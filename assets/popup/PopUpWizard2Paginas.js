/*
 * PopUpWizard2Paginas.js — Template de Wizard 2 p&aacute;ginas para PopUpBuilder
 *
 * Vari&aacute;vel injetada pelo PopUpBuilder via Java:
 *   var itensJson = '[{"id":1,"nome":"...","codigo":"...","descr":"...","subitens":[...]}]';
 *
 * REGRAS OBRIGAT&Oacute;RIAS:
 *   1. NUNCA usar comentarios com // — apenas blocos /* *\/
 *   2. NUNCA escrever chars acentuados no .html — usar entidades HTML
 *   3. build.gradle: include "${moduleName}/**" (nao apenas *.sql)
 *
 * ADAPTAR:
 *   - Substituir "item/subitem" pela entidade real (ex: entidade/campo)
 *   - Ajustar tipoLabel() e tipoCssClass() conforme os tipos do seu dom&iacute;nio
 *   - Substituir confirmar() pela l&oacute;gica final (ZIP, ServiceProxy, etc.)
 */

var itens = JSON.parse(itensJson);

/* Estado do wizard */
scope.pagina          = 1;
scope.itens           = itens;
scope.itemSelecionado = null;
scope.filtroP1        = '';
scope.filtroP2        = '';

/* Fun&ccedil;&otilde;es expostas no scope Angular */
scope.itensFiltrados          = itensFiltrados;
scope.selecionarItem          = selecionarItem;
scope.irParaPagina2           = irParaPagina2;
scope.voltar                  = voltar;
scope.selecionarTodos         = selecionarTodos;
scope.desmarcarTodos          = desmarcarTodos;
scope.toggleSubitem           = toggleSubitem;
scope.subitensFiltrados       = subitensFiltrados;
scope.subitensSelecionadosCount = subitensSelecionadosCount;
scope.tipoLabel               = tipoLabel;
scope.tipoCssClass            = tipoCssClass;
scope.confirmar               = confirmar;

/* Inicializa colunas redimension&aacute;veis na p&aacute;gina 1 */
setTimeout(function() { initResizableTable('tbl-p1'); }, 150);

/* Reinicializa ao navegar para p&aacute;gina 2 */
scope.$watch('pagina', function(newVal) {
    if (newVal === 2) {
        setTimeout(function() { initResizableTable('tbl-p2'); }, 100);
    }
});

/*
 * P&aacute;gina 1 — Sele&ccedil;&atilde;o de Item
 */

function itensFiltrados() {
    var filtro = (scope.filtroP1 || '').toUpperCase().trim();
    if (!filtro) return scope.itens;
    return scope.itens.filter(function(i) {
        return i.nome.toUpperCase().indexOf(filtro) !== -1
            || (i.codigo || '').toUpperCase().indexOf(filtro) !== -1
            || (i.descr  || '').toUpperCase().indexOf(filtro) !== -1;
    });
}

function selecionarItem(item) {
    scope.itemSelecionado = item;
}

function irParaPagina2() {
    if (!scope.itemSelecionado) {
        MessageUtils.showAlert(MessageUtils.TITLE_WARNING, 'Selecione um item antes de continuar!');
        return;
    }
    /* Inicializa todos os subitens como selecionados ao entrar na p&aacute;gina 2 */
    scope.itemSelecionado.subitens.forEach(function(s) { s.selecionado = true; });
    scope.filtroP2 = '';
    scope.pagina = 2;
}

/*
 * P&aacute;gina 2 — Sele&ccedil;&atilde;o / Configura&ccedil;&atilde;o de Subitens
 */

function voltar() {
    scope.pagina = 1;
}

function selecionarTodos() {
    subitensFiltrados().forEach(function(s) { s.selecionado = true; });
}

function desmarcarTodos() {
    subitensFiltrados().forEach(function(s) { s.selecionado = false; });
}

function toggleSubitem(sub) {
    sub.selecionado = !sub.selecionado;
}

function subitensFiltrados() {
    if (!scope.itemSelecionado) return [];
    var filtro = (scope.filtroP2 || '').toUpperCase().trim();
    if (!filtro) return scope.itemSelecionado.subitens;
    return scope.itemSelecionado.subitens.filter(function(s) {
        return s.nome.toUpperCase().indexOf(filtro) !== -1
            || (s.descr || '').toUpperCase().indexOf(filtro) !== -1;
    });
}

function subitensSelecionadosCount() {
    if (!scope.itemSelecionado) return 0;
    return scope.itemSelecionado.subitens.filter(function(s) { return s.selecionado; }).length;
}

/* Labels e estilos de tipo — ADAPTAR conforme o dom&iacute;nio */
function tipoLabel(tipo) {
    var mapa = { S: 'Texto', I: 'Inteiro', F: 'Decimal', D: 'Data', H: 'Hora', B: 'Bin&aacute;rio', O: 'Lista' };
    return mapa[tipo] || tipo || '?';
}

function tipoCssClass(tipo) {
    var mapa = { S: 'label-info', I: 'label-primary', F: 'label-default', D: 'label-success', H: 'label-default', B: 'label-danger', O: 'label-warning' };
    return mapa[tipo] || 'label-default';
}

/*
 * A&ccedil;&atilde;o final — ADAPTAR: gerar ZIP, chamar ServiceProxy, etc.
 */

function confirmar() {
    var selecionados = scope.itemSelecionado.subitens.filter(function(s) { return s.selecionado; });

    if (selecionados.length === 0) {
        MessageUtils.showAlert(MessageUtils.TITLE_WARNING, 'Selecione ao menos um item para continuar!');
        return;
    }

    var item = scope.itemSelecionado;

    /*
     * EXEMPLO A: gerar arquivo ZIP com metadata.xml
     * var xml  = construirMetadataXml(item, selecionados);
     * var nome = 'Metadados_' + item.codigo + '.zip';
     * gerarZip('metadata.xml', xml, nome);
     * scope.$dismiss();
     * MessageUtils.showInfo(MessageUtils.TITLE_INFORMATION, nome + ' gerado com ' + selecionados.length + ' item(s).');
     *
     * EXEMPLO B: chamar servi&ccedil;o backend
     * var ids = selecionados.map(function(s) { return s.id; }).join(',');
     * ServiceProxy.callService('modulo@Servico.processar', {params: {ITEM_ID: item.id, IDS: ids}}, {})
     *     .then(function(resp) {
     *         if (resp.responseBody.success) {
     *             scope.$dismiss();
     *             MessageUtils.showInfo(MessageUtils.TITLE_INFORMATION, 'Processado com sucesso!');
     *         } else {
     *             MessageUtils.showAlert(MessageUtils.TITLE_ERROR, resp.responseBody.message);
     *         }
     *     });
     */

    scope.$dismiss();
}

/*
 * Gera&ccedil;&atilde;o de ZIP client-side (puro JS, sem biblioteca externa)
 * Formato STORED (sem compress&atilde;o) com CRC-32 IEEE 802.3.
 * Incluir estas fun&ccedil;&otilde;es quando precisar de download ZIP.
 */

function gerarZip(nomeArquivoInterno, conteudo, nomeZip) {
    try {
        var zipBytes = criarZip(nomeArquivoInterno, conteudo);
        var blob = new Blob([zipBytes], { type: 'application/zip' });
        var url  = URL.createObjectURL(blob);
        var link = document.createElement('a');
        link.setAttribute('href', url);
        link.setAttribute('download', nomeZip);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        setTimeout(function() { URL.revokeObjectURL(url); }, 2000);
    } catch (e) {
        MessageUtils.showAlert(MessageUtils.TITLE_ERROR, 'Erro ao gerar ZIP: ' + (e.message || e));
    }
}

function criarZip(nomeArquivoInterno, conteudo) {
    var enc      = new TextEncoder();
    var fileData = enc.encode(conteudo);
    var fileName = enc.encode(nomeArquivoInterno);
    var crc     = crc32(fileData);
    var fSize   = fileData.length;
    var fnLen   = fileName.length;
    var now     = new Date();
    var dosDate = ((now.getFullYear() - 1980) << 9) | ((now.getMonth() + 1) << 5) | now.getDate();
    var dosTime = (now.getHours() << 11) | (now.getMinutes() << 5) | Math.floor(now.getSeconds() / 2);
    function u16(n) { return [(n) & 0xFF, (n >>> 8) & 0xFF]; }
    function u32(n) { return [(n) & 0xFF, (n >>> 8) & 0xFF, (n >>> 16) & 0xFF, (n >>> 24) & 0xFF]; }
    var localHdr = [].concat(
        [0x50,0x4B,0x03,0x04], u16(20), u16(0), u16(0),
        u16(dosTime), u16(dosDate), u32(crc), u32(fSize), u32(fSize), u16(fnLen), u16(0));
    var centralHdr = [].concat(
        [0x50,0x4B,0x01,0x02], u16(20), u16(20), u16(0), u16(0),
        u16(dosTime), u16(dosDate), u32(crc), u32(fSize), u32(fSize),
        u16(fnLen), u16(0), u16(0), u16(0), u16(0), u32(0), u32(localHdr.length + fnLen));
    var centralDirOffset = localHdr.length + fnLen + fSize;
    var centralDirSize   = centralHdr.length + fnLen;
    var endRec = [].concat(
        [0x50,0x4B,0x05,0x06], u16(0), u16(0), u16(1), u16(1),
        u32(centralDirSize), u32(centralDirOffset), u16(0));
    var fnArr   = Array.from(fileName);
    var dataArr = Array.from(fileData);
    return new Uint8Array(localHdr.concat(fnArr, dataArr, centralHdr, fnArr, endRec));
}

var CRC32_TABLE = (function() {
    var t = new Uint32Array(256);
    for (var n = 0; n < 256; n++) {
        var c = n;
        for (var k = 0; k < 8; k++) { c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1); }
        t[n] = c;
    }
    return t;
}());

function crc32(data) {
    var crc = 0xFFFFFFFF;
    for (var i = 0; i < data.length; i++) {
        crc = (crc >>> 8) ^ CRC32_TABLE[(crc ^ data[i]) & 0xFF];
    }
    return (crc ^ 0xFFFFFFFF) >>> 0;
}

/*
 * Colunas redimension&aacute;veis — arrastar a borda direita do cabe&ccedil;alho
 */

function initResizableTable(tableId) {
    var table = document.getElementById(tableId);
    if (!table) return;
    table.querySelectorAll('thead th .col-resizer').forEach(function(resizer) {
        var th = resizer.parentElement;
        var startX, startW;
        resizer.addEventListener('mousedown', function(e) {
            startX = e.pageX;
            startW = th.offsetWidth;
            resizer.classList.add('resizing');
            function onMove(ev) {
                th.style.width = Math.max(40, startW + ev.pageX - startX) + 'px';
            }
            function onUp() {
                resizer.classList.remove('resizing');
                document.removeEventListener('mousemove', onMove);
                document.removeEventListener('mouseup', onUp);
            }
            document.addEventListener('mousemove', onMove);
            document.addEventListener('mouseup', onUp);
            e.preventDefault();
            e.stopPropagation();
        });
    });
}
