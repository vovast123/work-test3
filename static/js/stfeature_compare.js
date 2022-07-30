/**
 * 2010-2019 Codezeel
 *
 * NOTICE OF LICENSE
 *
 * Tm feature for prestashop 1.7: compare, wishlist at product list 
 *
 * DISCLAIMER
 *
 *  @Module Name: CZ Feature
 *  @author    codezeel <support@codezeel.com>
 *  @copyright 2010-2019 codezeel
 *  @license   http://www.codezeel.com - prestashop template provider
 */
function createStCompareModalPopup(){$("body").append('<div class="modal st-modal st-modal-compare fade" tabindex="-1" role="dialog" aria-hidden="true"><div class="modal-dialog" role="document"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h5 class="modal-title text-xs-center"></h5></div></div></div></div>')}function StCompareButtonAction(){$(".st-compare-button").click((function(){if(!$(".st-compare-button.active").length){var a=compared_products.length,t=$(this).data("id-product"),o=productcompare_remove+'. <a href="'+productcompare_url+'" target="_blank"><strong>'+productcompare_viewlistcompare+".</strong></a>",e=productcompare_add+'. <a href="'+productcompare_url+'" target="_blank"><strong>'+productcompare_viewlistcompare+".</strong></a>",r=productcompare_max_item+'. <a href="'+productcompare_url+'" target="_blank"><strong>'+productcompare_viewlistcompare+".</strong></a>";$(this).addClass("active"),$(this).find(".st-compare-bt-loading").css({display:"block"});var c=$(this);$(this).hasClass("added")||$(this).hasClass("delete")?$.ajax({type:"POST",headers:{"cache-control":"no-cache"},url:productcompare_url,async:!0,cache:!1,data:{ajax:1,action:"remove",id_product:t},success:function(a){if(console.log(a),$(".ap-btn-compare .ap-total-compare").length){var e=parseInt($(".ap-btn-compare .ap-total-compare").data("compare-total"))-1;$(".ap-btn-compare .ap-total-compare").data("compare-total",e),$(".ap-btn-compare .ap-total-compare").text(e)}compared_products.splice($.inArray(parseInt(t),compared_products),1),c.hasClass("delete")?1==$(".leo-productscompare-item").length?window.location.replace(productcompare_url):$("td.product-"+t).fadeOut((function(){$(this).remove()})):($(".st-modal-compare .modal-title").html(o),$(".st-modal-compare").modal("show"),$(".st-compare-button[data-id-product="+t+"]").removeClass("added"),$(".st-compare-button[data-id-product="+t+"]").attr("title",buttoncompare_title_add),c.find(".st-compare-bt-loading").hide())},error:function(a,t,o){alert("TECHNICAL ERROR: \n\nDetails:\nError thrown: "+a+"\nText status: "+t)}}):a<comparator_max_item?$.ajax({type:"POST",headers:{"cache-control":"no-cache"},url:productcompare_url,async:!0,cache:!1,data:{ajax:1,action:"add",id_product:t},success:function(a){if($(".st-modal-compare .modal-title").html(e),$(".st-modal-compare").modal("show"),$(".ap-btn-compare .ap-total-compare").length){var o=parseInt($(".ap-btn-compare .ap-total-compare").data("compare-total"));alert(o);var r=o+1;$(".ap-btn-compare .ap-total-compare").data("compare-total",r),$(".ap-btn-compare .ap-total-compare").text(r)}compared_products.push(t),$(".st-compare-button[data-id-product="+t+"]").addClass("added"),$(".st-compare-button[data-id-product="+t+"]").attr("title",buttoncompare_title_remove),c.find(".st-compare-bt-loading").hide()},error:function(a,t,o){alert("TECHNICAL ERROR: \n\nDetails:\nError thrown: "+a+"\nText status: "+t)}}):($(".st-modal-compare .modal-title").html(r),$(".st-modal-compare").modal("show"),c.find(".st-compare-bt-loading").hide())}return!1}))}function activeEventModalCompare(){$(".st-modal-compare").on("hide.bs.modal",(function(a){$(".st-compare-button.active").length&&$(".st-compare-button.active").removeClass("active")})),$(".st-modal-compare").on("hidden.bs.modal",(function(a){$("body").css("padding-right","")})),$(".st-modal-compare").on("shown.bs.modal",(function(a){$(".quickview.modal").length&&$(".quickview.modal").modal("hide")}))}$(document).ready((function(){createStCompareModalPopup(),StCompareButtonAction(),prestashop.on("updateProductList",(function(){StCompareButtonAction()})),prestashop.on("clickQuickView",(function(){check_active_compare=setInterval((function(){$(".quickview.modal").length&&($(".quickview.modal").on("shown.bs.modal",(function(a){StCompareButtonAction()})),clearInterval(check_active_compare))}),300)})),activeEventModalCompare()}));