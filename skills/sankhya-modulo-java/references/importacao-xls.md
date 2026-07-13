# Importação de XLS/XLSX — Leitura de BLOB Sankhya

## Formato do BLOB com arquivo carregado

Campos de upload no Sankhya armazenam o conteúdo em coluna BLOB com cabeçalho de metadados:

```
__start_fileinformation__{"name":"planilha.xlsx","size":12345,"type":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet","lastModifiedDate":"May 26, 2026 18:39:23"}__end_fileinformation__<bytes reais do arquivo>
```

`BlobUtil` (ver `examples/Modelo_BlobUtil.java`) separa o cabeçalho dos bytes reais sem dependência externa.

---

## BlobUtil — API

```java
import br.com.sankhya.customizacao.utils.BlobUtil;

byte[] conteudoBlob = (byte[]) vo.getProperty("CAMPO_BLOB");
BlobUtil blob = new BlobUtil(conteudoBlob); // lança MGEModelException se BLOB vazio

blob.getFileName()             // "planilha.xlsx"
blob.getFileExtension()        // ".xlsx"  (com ponto, em minúsculas como declarado)
blob.getFileNamePure()         // "planilha"
blob.getFileSize()             // 12345  (declarado no cabeçalho, não verificado nos bytes)
blob.getFileType()             // "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
blob.getFileLastModifiedDate() // "May 26, 2026 18:39:23"
blob.getFileData()             // byte[] — bytes reais do arquivo
blob.getFileDataHEX()          // "504B0304..." — hex maiúsculo
```

---

## Detectar formato: XLS vs XLSX

```java
String ext = blob.getFileExtension().toLowerCase();
if (".xlsx".equals(ext)) {
    // Apache POI XSSFWorkbook
} else if (".xls".equals(ext)) {
    // Apache POI HSSFWorkbook
} else {
    throw new MGEModelException("Formato não suportado: " + ext + ". Enviar apenas .xls ou .xlsx.");
}
```

---

## Leitura com Apache POI

### XLSX — XSSFWorkbook

```java
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.apache.poi.ss.usermodel.*;

try (Workbook wb = new XSSFWorkbook(new java.io.ByteArrayInputStream(blob.getFileData()))) {
    Sheet aba = wb.getSheetAt(0);

    for (int i = 1; i <= aba.getLastRowNum(); i++) { // i=1 pula linha de cabeçalho
        Row linha = aba.getRow(i);
        if (linha == null) continue;

        String campo1    = getCellString(linha, 0);
        BigDecimal valor = getCellBigDecimal(linha, 1);
        // processar...
    }
}
```

### XLS — HSSFWorkbook

```java
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.*;

try (Workbook wb = new HSSFWorkbook(new java.io.ByteArrayInputStream(blob.getFileData()))) {
    Sheet aba = wb.getSheetAt(0);
    // mesma API do XSSFWorkbook acima
}
```

### Helpers de leitura de Cell

```java
import org.apache.poi.ss.usermodel.*;

private static String getCellString(Row row, int col) {
    Cell cell = row.getCell(col, Row.MissingCellPolicy.RETURN_BLANK_AS_NULL);
    if (cell == null) return "";
    switch (cell.getCellType()) {
        case STRING:  return cell.getStringCellValue().trim();
        case NUMERIC: return String.valueOf((long) cell.getNumericCellValue());
        case BOOLEAN: return String.valueOf(cell.getBooleanCellValue());
        default:      return "";
    }
}

private static BigDecimal getCellBigDecimal(Row row, int col) {
    Cell cell = row.getCell(col, Row.MissingCellPolicy.RETURN_BLANK_AS_NULL);
    if (cell == null || cell.getCellType() != CellType.NUMERIC) return BigDecimal.ZERO;
    return BigDecimal.valueOf(cell.getNumericCellValue());
}
```

---

## Padrão completo: ActionButton → Component

### ActionButton

```java
@Override
public void doAction(ContextoAcao ctx) throws Exception {
    if (ctx.getLinhas().length != 1) {
        ctx.setMensagemRetorno("Selecione exatamente um registro!");
        return;
    }

    BigDecimal id = BigDecimalUtil.getBigDecimal(ctx.getLinhas()[0].getCampo("ID_CAMPO"));

    JapeSession.SessionHandle hnd = null;
    try {
        hnd = JapeSession.open();
        NomeComponent component = new NomeComponent();
        String resultado = component.processarPlanilha(id);
        ctx.setMensagemRetorno(resultado);
    } catch (NomeDemandaException e) {
        throw MGEModelException.prettyMsg(e.getMessage(), e);
    } catch (Exception e) {
        throw MGEModelException.prettyMsg("Erro ao importar planilha: <br>" + e.getMessage(), e);
    } finally {
        JapeSession.close(hnd);
    }
}
```

### Component — leitura e despacho

```java
public String processarPlanilha(BigDecimal id) throws Exception {
    DynamicVO vo = JapeFactory.dao("AD_MINHAENTIDADE").findByPK(id);
    if (vo == null) throw new NomeDemandaException("Registro não encontrado: " + id);

    byte[] conteudoBlob = (byte[]) vo.getProperty("CAMPO_BLOB");
    BlobUtil blob = new BlobUtil(conteudoBlob);

    String ext = blob.getFileExtension().toLowerCase();
    if (!".xls".equals(ext) && !".xlsx".equals(ext)) {
        throw new NomeDemandaException("Formato inválido: " + ext + ". Enviar apenas .xls ou .xlsx.");
    }

    try (Workbook wb = criarWorkbook(blob)) {
        return importarLinhas(wb.getSheetAt(0), id);
    }
}

private Workbook criarWorkbook(BlobUtil blob) throws Exception {
    java.io.InputStream is = new java.io.ByteArrayInputStream(blob.getFileData());
    return ".xlsx".equals(blob.getFileExtension().toLowerCase())
            ? new XSSFWorkbook(is)
            : new HSSFWorkbook(is);
}

private String importarLinhas(Sheet aba, BigDecimal id) throws Exception {
    int importados = 0;
    for (int i = 1; i <= aba.getLastRowNum(); i++) {
        Row linha = aba.getRow(i);
        if (linha == null) continue;
        // persistir via repository...
        importados++;
    }
    return importados + " linha(s) importada(s) com sucesso.";
}
```

---

## Comportamento sem cabeçalho Sankhya

Se o BLOB não contiver `__start_fileinformation__` (arquivo bruto, não enviado pelo upload do Sankhya):

| Método | Retorno |
|---|---|
| `getFileName()` | `"arquivo"` |
| `getFileSize()` | `conteudoBlob.length` |
| `getFileType()` | `""` |
| `getFileLastModifiedDate()` | `""` |
| `getFileData()` | array completo sem truncagem |

---

## MIME types de referência

| Formato | MIME type |
|---|---|
| `.xlsx` | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| `.xls`  | `application/vnd.ms-excel` |
| `.csv`  | `text/csv` |
| `.pdf`  | `application/pdf` |

---

## Dependências Apache POI (Gradle)

```groovy
implementation 'org.apache.poi:poi:5.2.5'        // HSSFWorkbook (.xls)
implementation 'org.apache.poi:poi-ooxml:5.2.5'  // XSSFWorkbook (.xlsx)
```

> Verificar se a versão já está no classpath do Sankhya antes de adicionar dependência própria.
> O Sankhya pode incluir uma versão mais antiga — nesse caso, alinhar a versão ou usar a fornecida pelo servidor.
