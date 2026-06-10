package br.com.sankhya.dstech.nomedemanda.dto;

import java.math.BigDecimal;

/**
 * DTO de NomeDemanda.
 *
 * Usar quando:
 *   - Precisar agrupar campos para trafegar entre camadas (event → service, job → service).
 *   - Um DynamicVO não for suficiente para representar o que precisas
 *     (ex: dados combinados de mais de uma entidade).
 *   - Mapear resultado de queries complexas com campos calculados ou de múltiplas tabelas.
 *
 * Não usar quando:
 *   - Um DynamicVO único já representa o que precisas — não criar DTO só por hábito.
 *   - A operação for simples o suficiente para passar apenas o ID entre camadas.
 *
 * DTOs não têm lógica de negócio. Apenas getters/setters e construtores.
 */
public class NomeDto {

    private BigDecimal id;
    private BigDecimal idPai;
    private BigDecimal codigoEmpresa;
    private String status;
    private String descricao;

    // -------------------------------------------------------------------------
    // Construtor a partir de DynamicVO — usado no event/ para extrair dados
    // antes de delegar para o service
    // -------------------------------------------------------------------------

    public NomeDto(br.com.sankhya.jape.vo.DynamicVO vo) throws Exception {
        this.id           = vo.asBigDecimal("ID");
        this.idPai        = vo.asBigDecimal("ID_PAI");
        this.codigoEmpresa = vo.asBigDecimal("CODEMP");
        this.status       = vo.asString("STATUS");
        this.descricao    = vo.asString("DESCRICAO");
    }

    public NomeDto() {}

    // -------------------------------------------------------------------------
    // Getters e setters
    // -------------------------------------------------------------------------

    public BigDecimal getId()                          { return id; }
    public void setId(BigDecimal id)                   { this.id = id; }

    public BigDecimal getIdPai()                       { return idPai; }
    public void setIdPai(BigDecimal idPai)             { this.idPai = idPai; }

    public BigDecimal getCodigoEmpresa()               { return codigoEmpresa; }
    public void setCodigoEmpresa(BigDecimal codEmp)    { this.codigoEmpresa = codEmp; }

    public String getStatus()                          { return status; }
    public void setStatus(String status)               { this.status = status; }

    public String getDescricao()                       { return descricao; }
    public void setDescricao(String descricao)         { this.descricao = descricao; }
}
