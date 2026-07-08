# SessionFile

**Pacote:** `com.sankhya.util.SessionFile`
> Verificado via `javap` em `sanutil-4.35.jar`

```java
import com.sankhya.util.SessionFile;
import java.io.File;
```

> `SessionFile` estende `DiskFileItem` (Apache Commons FileUpload).
> Usar para gerar arquivos temporários de sessão e retorná-los ao usuário via `Action Button`.

---

## Criar SessionFile (para retornar ao usuário)

```java
// A partir de bytes — mais comum ao gerar PDF/Excel programaticamente
byte[] conteudoPdf = gerarPdf(); // JasperPrint, iText, etc.
SessionFile arquivo = SessionFile.createSessionFile(
    "relatorio.pdf",         // nome do arquivo exibido ao usuário
    "application/pdf",       // MIME type
    conteudoPdf              // conteúdo em bytes
); // throws IOException

// A partir de File existente em disco
File source = new File("/tmp/gerado.xlsx");
SessionFile arqXls = SessionFile.createSessionFile(
    "planilha.xlsx",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    source
); // throws IOException
```

### MIME types comuns

| Formato | MIME type |
|---|---|
| PDF | `application/pdf` |
| Excel (.xlsx) | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| Excel (.xls) | `application/vnd.ms-excel` |
| CSV | `text/csv` |
| ZIP | `application/zip` |
| XML | `application/xml` |

---

## Criar arquivo temporário (para processar antes de retornar)

```java
// Arquivo temporário com extensão
File temp = SessionFile.buildTempFile(".pdf");                // throws Exception

// Arquivo temporário com conteúdo inicial em bytes
File temp2 = SessionFile.buildTempFile(conteudoBytes, ".xlsx"); // throws Exception

// Arquivo temporário sem extensão
File temp3 = SessionFile.buildTempFile();                    // throws Exception
```

---

## Diretório temporário da sessão

```java
// Obter diretório onde arquivos de sessão são armazenados
File dir = SessionFile.getTempViewerFileDir();
// Útil para construir caminho antes de criar o arquivo
File arquivo = new File(dir, "saida_" + System.currentTimeMillis() + ".csv");
```

---

## Configurar envio por e-mail

```java
SessionFile sf = SessionFile.createSessionFile("doc.pdf", "application/pdf", bytes);
sf.setCanSendViaEmail(true);   // throws Exception — permite que o usuário envie por e-mail
boolean podeEmail = sf.isCanSendViaEmail();
```

---

## Uso típico em Action Button

```java
@Override
public void execute(ContextoAcao ctx) throws Exception {
    byte[] pdf = gerarRelatorioPdf(ctx);

    SessionFile arquivo = SessionFile.createSessionFile(
        "apuracao_icms.pdf",
        "application/pdf",
        pdf
    );

    ctx.setReturnFile(arquivo); // retorna o arquivo para download no cliente
}
```

---

## Antipadrões

```java
// ERRADO — criar File temporário em caminho fixo
File temp = new File("C:/temp/relatorio.pdf"); // não funciona no servidor

// CORRETO — usar diretório gerenciado pela sessão Sankhya
File temp = SessionFile.buildTempFile(".pdf");

// ERRADO — retornar File diretamente
ctx.setReturnFile(new File("/tmp/saida.pdf")); // tipo incompatível

// CORRETO — criar SessionFile antes de retornar
SessionFile sf = SessionFile.createSessionFile("saida.pdf", "application/pdf", bytes);
ctx.setReturnFile(sf);
```
