# TimeUtils

**Pacote:** `com.sankhya.util.TimeUtils`
> Verificado via `javap` em `sanutil-4.35.jar`

> **Atenção:** pacote real é `com.sankhya.util` (não `br.com.sankhya.util`).

```java
import com.sankhya.util.TimeUtils;
import java.sql.Timestamp;
import java.util.Calendar;
```

---

## Obter data/hora atual

```java
Timestamp agora = TimeUtils.getNow();          // Timestamp atual
long hoje        = TimeUtils.getToday();        // long — útil para setar em DynamicVO
Timestamp seguro = TimeUtils.getValueOrNow(ts); // retorna ts, ou getNow() se null
```

---

## Converter parâmetro de ação (Object → java.sql.Date)

```java
import java.sql.Date;

// ctx.getParam() retorna Object — tipo varia conforme config do parâmetro na entidade
// convertToOnlyDate aceita Object e retorna TimeUtils$OnlyDate (extends Timestamp)
// asSqlDate() converte para java.sql.Date compatível com Repository/Component
Date dtIni = TimeUtils.convertToOnlyDate(ctx.getParam("P_DTINI")).asSqlDate();
Date dtFin = TimeUtils.convertToOnlyDate(ctx.getParam("P_DTFIN")).asSqlDate();
```

---

## Construir Timestamp a partir de String ou partes

```java
Timestamp ts1 = TimeUtils.buildTimestamp("2026-05-22");          // "yyyy-MM-dd"
Timestamp ts2 = TimeUtils.toTimestamp("22/05/2026", "dd/MM/yyyy");
Timestamp ts3 = TimeUtils.toTimestamp("2026-05-22");             // ISO sem hora
Timestamp ts4 = TimeUtils.buildTimestampRFC3339("2026-05-22T00:00:00Z");
Timestamp ts5 = TimeUtils.buildData(2026, 5, 22);                // ano, mês (1-12), dia
Timestamp ts6 = TimeUtils.bigDecimal2Timestamp(bdData);          // BigDecimal → Timestamp
```

---

## Aritmética de datas

```java
// add/set com Calendar.DAY_OF_MONTH, Calendar.MONTH, Calendar.YEAR, etc.
long amanha    = TimeUtils.add(TimeUtils.getToday(), Calendar.DAY_OF_MONTH, 1);
long mesSeg    = TimeUtils.add(TimeUtils.getToday(), Calendar.MONTH, 1);
long fixDia    = TimeUtils.set(TimeUtils.getToday(), Calendar.DAY_OF_MONTH, 1);

// Overloads com Timestamp
Timestamp t2   = TimeUtils.dataAdd(ts, Calendar.DAY_OF_MONTH, 5);
Timestamp t3   = TimeUtils.dataAddDay(ts, 10);
Timestamp t4   = TimeUtils.dataAddYear(ts, 1);

// Dias úteis
long proxUtil  = TimeUtils.addWorkingDays(TimeUtils.getToday(), 5);
long proxUtil2 = TimeUtils.getProximoDiaUtil(TimeUtils.getToday()); // throws Exception
```

---

## Início e fim de períodos

```java
Timestamp inicioMes  = TimeUtils.getMonthStart(ts);
Timestamp fimMes     = TimeUtils.getMonthEnd(ts);
Timestamp anoInicio  = TimeUtils.getYearStart(ts);
Timestamp refAnt     = TimeUtils.getReferenciaAnterior(ts);        // primeiro dia do mês anterior
Timestamp ultDiaAnt  = TimeUtils.getUltimoDiaDoMesRefAnterior(ts); // último dia do mês anterior
Timestamp ultDiaMesAnt = TimeUtils.ultimoDiaMesAnterior(ts);

long inicioMesL = TimeUtils.getMonthStart(longTs);
long fimMesL    = TimeUtils.getMonthEnd(longTs);
long inicioSem  = TimeUtils.getDayStart(longTs);
long fimSem     = TimeUtils.getDayEnd(longTs);
long inicioProxMes = TimeUtils.getNextMonthStart(longTs);
```

---

## Extrair partes de uma data

```java
int dia       = TimeUtils.getDay(ts);
int mes       = TimeUtils.getMonth(ts);       // 0-11 (padrão Calendar)
int ano       = TimeUtils.getYear(ts);
int semana    = TimeUtils.getWeekOfYear(ts);
int diaSemana = TimeUtils.dayOfWeek(ts);      // 1=Dom..7=Sáb
int diasMes   = TimeUtils.getLastDayOfMonth(ts);
```

---

## Diferença entre datas

```java
int dias   = TimeUtils.getDifference(ts1, ts2);           // em dias
long min   = TimeUtils.getDifferenceInMinutes(ts1, ts2);
long horas = TimeUtils.getDifferenceInHour(ts1, ts2);
long meses = TimeUtils.getDifferenceInMonths(ts1, ts2);
int cmp    = TimeUtils.compareOnlyDates(ts1, ts2);        // -1, 0, 1
boolean same = TimeUtils.compareDatesEqualsYearMonth(ts1, ts2);
```

---

## Zerar partes de data/hora

```java
Timestamp soData  = TimeUtils.clearTime(ts);      // zera horas, min, seg, ms
long soDataL      = TimeUtils.clearTime(longTs);
long soHora       = TimeUtils.clearDate(longTs);  // zera dia, mês, ano
Timestamp custom  = TimeUtils.clearFields(ts, Calendar.HOUR_OF_DAY, Calendar.MINUTE);
```

---

## Verificações

```java
boolean fimSemana   = TimeUtils.isWeekend(longTs);         // throws Exception
boolean primeiroDia = TimeUtils.isFirstDayOfMonth(longTs);
boolean ultimoDia   = TimeUtils.isLastDayOfMonth(longTs);
```

---

## Conversões numéricas

```java
BigDecimal bd   = TimeUtils.timestamp2BigDecimal(ts);
Timestamp ts    = TimeUtils.bigDecimal2Timestamp(bd);      // throws Exception
long minutos    = TimeUtils.timestamp2Minutes(longTs);
long ts2        = TimeUtils.minutes2Timestamp(minutos);
```

---

## Formatação para exibição

```java
String ddmmyyyy     = TimeUtils.formataDDMMYYYY(ts);         // "22/05/2026"
String ddmmyy       = TimeUtils.formataDDMMYY(ts);           // "22/05/26"
String mmyyyy       = TimeUtils.formataMMYYYY(ts);           // "05/2026"
String yyyymmdd     = TimeUtils.formataYYYYMMDD(ts);         // "20260522"
String completo     = TimeUtils.formataDDMMYYYYHHMMSS(ts);   // "22/05/2026 10:30:00"
String semSeg       = TimeUtils.formataDDMMYYYYHHMM(ts);     // "22/05/2026 10:30"
String hora         = TimeUtils.formataHHMM(ts);             // "10:30"
String horaCompleta = TimeUtils.formataHHMMSS(ts);           // "10:30:00"
String rfc          = TimeUtils.formataRFC3339(ts);          // "2026-05-22T10:30:00Z"
String porExtenso   = TimeUtils.dataPorExtenso(ts);          // "22 de maio de 2026"
String mes          = TimeUtils.mesext(ts);                  // "maio"
```
