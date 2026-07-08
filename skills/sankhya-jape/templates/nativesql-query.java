// Template: NativeSql com parametros nomeados e liberacao de recursos
// Use quando: SQL complexo (JOIN/GROUP BY/subquery) que nao se expressa bem via FinderWrapper/EntityQuery

import java.math.BigDecimal;
import java.sql.ResultSet;
import br.com.sankhya.jape.dao.JdbcWrapper;
import br.com.sankhya.jape.sql.NativeSql;
import com.sankhya.util.JdbcUtils;

public class QueryExemplo {

    public BigDecimal somarValorPorTipo(JdbcWrapper jdbc, String tipMov, java.sql.Date dataInicio) throws Exception {
        NativeSql q = null;
        ResultSet rs = null;
        try {
            q = new NativeSql(jdbc);
            q.appendSql("SELECT SUM(VLRNOTA) AS TOTAL FROM TGFCAB ");
            q.appendSql("WHERE TIPMOV = :TIPMOV ");
            q.appendSql("  AND DTNEG >= :DT_INI");

            q.setNamedParameter("TIPMOV", tipMov);
            q.setNamedParameter("DT_INI", dataInicio);

            rs = q.executeQuery();
            if (rs.next()) {
                return rs.getBigDecimal("TOTAL");
            }
            return BigDecimal.ZERO;
        } finally {
            JdbcUtils.closeResultSet(rs);
            NativeSql.releaseResources(q);
        }
    }
}
