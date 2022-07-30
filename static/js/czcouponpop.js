/**
 * 2016-2020 Codezeel
 *
 * NOTICE OF LICENSE
 *
 * DISCLAIMER
 *
 *  @Module Name: CZ CouponPop Module
 *  @author    codezeel <support@codezeel.com>
 *  @copyright 2010-2019 codezeel
 *  @license   http://www.codezeel.com - prestashop template provider
 */
function showDialog(){$.ajax({type:"POST",cache:!1,url:cz_coupon_url+"/front-end-ajax.php",dataType:"json",data:{task:"showPopup"},complete:function(){},success:function(e){}}),setTimeout((function(){$("#overlay").show(),$(".newsletter-main").show()}),500)}function closeDialog(e){var t={task:"cancelRegisNewslette1",cookies_time:e};$("#notshow").is(":checked")?t.notshow="1":t.notshow="0",$.ajax({type:"POST",cache:!1,url:cz_coupon_url+"/front-end-ajax.php",dataType:"json",data:t,complete:function(){},success:function(e){}}),setTimeout((function(){$("#overlay").hide(),$(".newsletter-main").hide()}),500)}function check_email(e){return emailRegExp=/^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.([a-z]){2,4})$/,!!emailRegExp.test(e)}function regisNewsletter(){var e={task:"regisNewsletter",action:0},t=$("#newsletter_input_email").val();if(1!=check_email(t))return $("#regisNewsletterMessage").html('<p class="alert alert-danger">'+enterEmail+"</p>"),!1;e.email=t,$("#regisNewsletterMessage").html(""),$("#notshow").is(":checked")?e.notshow="1":e.notshow="0",$.ajax({type:"POST",cache:!1,url:cz_coupon_url+"/front-end-ajax.php",dataType:"json",data:e,complete:function(){},success:function(e){if(e.indexOf("@")>0){var t=e.substring(e.indexOf("@")+1,e.length);$("#regisNewsletterMessage").html('<p class="alert alert-success">'+t+"</p>")}else $("#regisNewsletterMessage").html('<p class="alert alert-warning">'+e+"</p>");$("#coupon-text-before").hide(),$("#coupon-text-after").show()},error:function(e,t,a){alert("Status: "+t),alert("Error: "+a)}})}$(document).ready((function(){})),$((function(){$("html").bind("mouseleave",(function(){showDialog(),$("html").unbind("mouseleave")}))}));