/**
 * 2007-2019 PrestaShop
 *
 * NOTICE OF LICENSE
 *
 * This source file is subject to the Academic Free License (AFL 3.0)
 * that is bundled with this package in the file LICENSE.txt.
 * It is also available through the world-wide-web at this URL:
 * http://opensource.org/licenses/afl-3.0.php
 * If you did not receive a copy of the license and are unable to
 * obtain it through the world-wide-web, please send an email
 * to license@prestashop.com so we can send you a copy immediately.
 *
 * DISCLAIMER
 *
 * Do not edit or add to this file if you wish to upgrade PrestaShop to newer
 * versions in the future. If you wish to customize PrestaShop for your
 * needs please refer to http://www.prestashop.com for more information.
 *
 * @author    PrestaShop SA <contact@prestashop.com>
 * @copyright 2007-2019 PrestaShop SA
 * @license   http://opensource.org/licenses/afl-3.0.php  Academic Free License (AFL 3.0)
 * International Registered Trademark & Property of PrestaShop SA
 */
$(window).ready((function(){$(".blockreassurance_product img.svg, .blockreassurance img.svg").each((function(){var s=$(this),a=s.attr("id"),i=s.attr("class"),r=s.attr("src");$.ajax({url:r,type:"GET",success:function(t){if($.isXMLDoc(t)){var l=$(t).find("svg");l=void 0!==a?l.attr("id",a):l,(l=void 0!==i?l.attr("class",i+" replaced-svg"):l.attr("class"," replaced-svg")).removeClass("invisible"),(l=(l=l.attr("data-img-url",r)).removeAttr("xmlns:a")).find("path[fill]").attr("fill",psr_icon_color),l.find("path:not([fill])").css("fill",psr_icon_color),s.replaceWith(l)}s.removeClass("invisible")}})}))}));