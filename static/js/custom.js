function additionalCarousel(e){var t=$(e);t.owlCarousel({items:4,itemsDesktop:[1259,4],itemsDesktopSmall:[1199,3],itemsTablet:[767,2],itemsMobile:[320,1]}),$(".additional_next").click((function(){t.trigger("owl.next")})),$(".additional_prev").click((function(){t.trigger("owl.prev")}))}function hoverimagedir(){$(".image").each((function(){$(this).hoverdir()}))}$(document).ready((function(){bindGrid(),additionalCarousel("#main .additional-carousel"),hoverimagedir(),prestashop.on("updateProductList",(function(){hoverimagedir()})),$(".products-section-title").wrapInner("<span></span>"),$(".cart_block.dropdown-menu").on("click",(function(e){e.stopPropagation()})),$("#mainmenu-toggle").click((function(e){e.stopPropagation(),$(".mobile_main_menu").toggle()})),$("#menu-icon").on("click",(function(){$(this).toggleClass("active")})),$('input[name="email"], #search_widget input[type="text"]').focus((function(){$(this).data("placeholder",$(this).attr("placeholder")).attr("placeholder","")})).blur((function(){$(this).attr("placeholder",$(this).data("placeholder"))})),$(".search_button").click((function(e){$(this).toggleClass("active"),e.stopPropagation(),$(".search_toggle").toggle(),$(".search-widget form input[type=text]").focus()})),$(".search_toggle").on("click",(function(e){e.stopPropagation()})),$("nav.breadcrumb").appendTo("#content-wrapper .breadcrumb"),/Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent)?$(".parallax").sitManParallex({invert:!0}):$(".parallax").length&&$(".parallax").sitManParallex({invert:!1});var e=$(".horizontal-menu ul#top-menu > li");e.slice(5,e.length).wrapAll('<li class="category more_menu" id="more_menu"><div id="top_moremenu" class="popover sub-menu js-sub-menu collapse"><ul class="top-menu more_sub_menu">'),$(".horizontal-menu ul#top-menu .more_menu").prepend('<a href="#" class="dropdown-item" data-depth="0"><span class="pull-xs-right hidden-md-up"><span data-target="#top_moremenu" data-toggle="collapse" class="navbar-toggler collapse-icons"><i class="material-icons add">&#xE313;</i><i class="material-icons remove">&#xE316;</i></span></span></span>More</a>'),$(".horizontal-menu ul#top-menu .more_menu").mouseover((function(){$(this).children("div").css("display","block")})).mouseout((function(){$(this).children("div").css("display","none")}));var t=$("#czverticalmenublock ul#top-menu > li");t.length>12&&$("#czverticalmenublock ul#top-menu").append('<li class="more_menu"><a href="#" class="vertical-menu-item" data-depth="0">More Categories<span class="more_category"><i class="fa-icon add"></i></span></a></li>'),$("#czverticalmenublock ul#top-menu .more_menu").click((function(e){e.preventDefault(),$(this).hasClass("active")?(t.each((function(e){e>=12&&$(this).slideUp(200)})),$(this).removeClass("active"),$("#czverticalmenublock ul#top-menu .more_menu").html('<a href="#" class="vertical-menu-item" data-depth="0">More Categories<span class="more_category"><i class="fa-icon add"></i></span></a>')):(t.each((function(e){e>=12&&$(this).slideDown(200)})),$(this).addClass("active"),$("#czverticalmenublock ul#top-menu .more_menu").html('<a href="#" class="vertical-menu-item" data-depth="0">Less Categories<span class="more_category"><i class="fa-icon remove">&nbsp;</i></span></a>'))})),t.each((function(e){e>=12&&$(this).css("display","none")}))})),$(window).load((function(){$(".loadingdiv").removeClass("spinner")})),$(window).load((function(){$(".flexslider").length>0&&$(".flexslider").flexslider({slideshowSpeed:$(".flexslider").data("interval"),pauseOnHover:$(".flexslider").data("pause"),animation:"Slide"})})),$(window).scroll((function(){$(this).scrollTop()>500?$(".top_button").fadeIn(500):$(".top_button").fadeOut(500)})),$(".top_button").click((function(e){e.preventDefault(),$("html, body").animate({scrollTop:0},800)}));var czblog=$("#blog-carousel");czblog.owlCarousel({items:3,itemsDesktop:[1199,3],itemsDesktopSmall:[991,2],itemsTablet:[400,1],itemsMobile:[400,1]}),$(".blog_next").click((function(){czblog.trigger("owl.next")})),$(".blog_prev").click((function(){czblog.trigger("owl.prev")}));var czfeature=$("#feature-carousel");czfeature.owlCarousel({items:5,itemsDesktop:[1199,4],itemsDesktopSmall:[991,3],itemsTablet:[580,2],itemsMobile:[350,1]}),$(".feature_next").click((function(){czfeature.trigger("owl.next")})),$(".feature_prev").click((function(){czfeature.trigger("owl.prev")}));var cznewproduct=$("#newproduct-carousel");cznewproduct.owlCarousel({items:5,itemsDesktop:[1199,4],itemsDesktopSmall:[991,3],itemsTablet:[580,2],itemsMobile:[350,1]}),$(".newproduct_next").click((function(){cznewproduct.trigger("owl.next")})),$(".newproduct_prev").click((function(){cznewproduct.trigger("owl.prev")}));var czbestseller=$("#bestseller-carousel");czbestseller.owlCarousel({items:5,itemsDesktop:[1199,4],itemsDesktopSmall:[991,3],itemsTablet:[580,2],itemsMobile:[350,1]}),$(".bestseller_next").click((function(){czbestseller.trigger("owl.next")})),$(".bestseller_prev").click((function(){czbestseller.trigger("owl.prev")}));var czspecial=$("#special-carousel");czspecial.owlCarousel({items:5,itemsDesktop:[1199,4],itemsDesktopSmall:[991,3],itemsTablet:[580,2],itemsMobile:[350,1]}),$(".special_next").click((function(){czspecial.trigger("owl.next")})),$(".special_prev").click((function(){czspecial.trigger("owl.prev")}));var czaccessories=$("#accessories-carousel");czaccessories.owlCarousel({items:5,itemsDesktop:[1199,4],itemsDesktopSmall:[991,3],itemsTablet:[580,2],itemsMobile:[350,1]}),$(".accessories_next").click((function(){czaccessories.trigger("owl.next")})),$(".accessories_prev").click((function(){czaccessories.trigger("owl.prev")}));var czproductscategory=$("#productscategory-carousel");czproductscategory.owlCarousel({items:5,itemsDesktop:[1199,4],itemsDesktopSmall:[991,3],itemsTablet:[580,2],itemsMobile:[350,1]}),$(".productscategory_next").click((function(){czproductscategory.trigger("owl.next")})),$(".productscategory_prev").click((function(){czproductscategory.trigger("owl.prev")}));var czviewed=$("#viewed-carousel");czviewed.owlCarousel({items:5,itemsDesktop:[1199,4],itemsDesktopSmall:[991,3],itemsTablet:[580,2],itemsMobile:[350,1]}),$(".viewed_next").click((function(){czviewed.trigger("owl.next")})),$(".viewed_prev").click((function(){czviewed.trigger("owl.prev")}));var czcrosssell=$("#crosssell-carousel");czcrosssell.owlCarousel({items:5,itemsDesktop:[1199,4],itemsDesktopSmall:[991,3],itemsTablet:[580,2],itemsMobile:[350,1]}),$(".crosssell_next").click((function(){czcrosssell.trigger("owl.next")})),$(".crosssell_prev").click((function(){czcrosssell.trigger("owl.prev")}));var czbrand=$("#brand-carousel");czbrand.owlCarousel({items:7,itemsDesktop:[1199,5],itemsDesktopSmall:[767,4],itemsTablet:[650,3],itemsTabletSmall:[480,2],itemsMobile:[320,1]}),$(".brand_next").click((function(){czbrand.trigger("owl.next")})),$(".brand_prev").click((function(){czbrand.trigger("owl.prev")}));var cztestimonial=$("#testimonial-carousel");cztestimonial.owlCarousel({autoPlay:!1,singleItem:!0}),$(".cztestimonial_next").click((function(){cztestimonial.trigger("owl.next")})),$(".cztestimonial_prev").click((function(){cztestimonial.trigger("owl.prev")}));var czcategoryimagelist=$("#czcategoryimagelist-carousel");function bindGrid(){var e=$.totalStorage("display");e&&"grid"!=e?display(e):$(".display").find("li#grid").addClass("selected"),$(document).on("click","#grid",(function(e){e.preventDefault(),display("grid")})),$(document).on("click","#list",(function(e){e.preventDefault(),display("list")}))}function display(e){"list"==e?($("#products ul.product_list").removeClass("grid").addClass("list row"),$("#products .product_list > li").removeClass("col-xs-12 col-sm-6 col-md-6 col-lg-4").addClass("col-xs-12"),$("#products .product_list > li").each((function(e,t){var i="";i='<div class="product-miniature js-product-miniature" data-id-product="'+$(t).find(".product-miniature").data("id-product")+'" data-id-product-attribute="'+$(t).find(".product-miniature").data("id-product-attribute")+'" itemscope itemtype="http://schema.org/Product">',i+='<div class="thumbnail-container col-xs-4 col-xs-5 col-md-3">'+$(t).find(".thumbnail-container").html()+"</div>",i+='<div class="product-description center-block col-xs-4 col-xs-7 col-md-9">',i+='<div class="brand-title" itemprop="name">'+$(t).find(".brand-title").html()+"</div>",i+='<h3 class="h3 product-title" itemprop="name">'+$(t).find("h3").html()+"</h3>",null!=$(t).find(".comments_note").html()&&(i+='<div class="comments_note">'+$(t).find(".comments_note").html()+"</div>");var o=$(t).find(".product-price-and-shipping").html();null!=o&&(i+='<div class="product-price-and-shipping">'+o+"</div>"),i+='<div class="product-detail">'+$(t).find(".product-detail").html()+"</div>";var l=$(t).find(".highlighted-informations").html();null!=l&&(i+='<div class="highlighted-informations">'+l+"</div>"),i+='<div class="product-actions">'+$(t).find(".product-actions").html()+"</div>",i+="</div>",i+="</div>",$(t).html(i)})),$(".display").find("li#list").addClass("selected"),$(".display").find("li#grid").removeAttr("class"),$.totalStorage("display","list"),"undefined"!=typeof StWishlistButtonAction&&StWishlistButtonAction(),"undefined"!=typeof StCompareButtonAction&&StCompareButtonAction(),hoverimagedir()):($("#products ul.product_list").removeClass("list").addClass("grid row"),$("#products .product_list > li").removeClass("col-xs-12").addClass("col-xs-12 col-sm-6 col-md-6 col-lg-4"),$("#products .product_list > li").each((function(e,t){var i="";i+='<div class="product-miniature js-product-miniature" data-id-product="'+$(t).find(".product-miniature").data("id-product")+'" data-id-product-attribute="'+$(t).find(".product-miniature").data("id-product-attribute")+'" itemscope itemtype="http://schema.org/Product">',i+='<div class="thumbnail-container">'+$(t).find(".thumbnail-container").html()+"</div>",i+='<div class="product-description">',i+='<div class="brand-title" itemprop="name">'+$(t).find(".brand-title").html()+"</div>",i+='<h3 class="h3 product-title" itemprop="name">'+$(t).find("h3").html()+"</h3>";var o=$(t).find(".product-price-and-shipping").html();null!=o&&(i+='<div class="product-price-and-shipping">'+o+"</div>"),null!=$(t).find(".comments_note").html()&&(i+='<div class="comments_note">'+$(t).find(".comments_note").html()+"</div>"),i+='<div class="product-detail">'+$(t).find(".product-detail").html()+"</div>",i+='<div class="product-actions">'+$(t).find(".product-actions").html()+"</div>";var l=$(t).find(".highlighted-informations").html();null!=l&&(i+='<div class="highlighted-informations">'+l+"</div>"),i+="</div>",i+="</div>",$(t).html(i)})),$(".display").find("li#grid").addClass("selected"),$(".display").find("li#list").removeAttr("class"),$.totalStorage("display","grid"),"undefined"!=typeof StWishlistButtonAction&&StWishlistButtonAction(),"undefined"!=typeof StCompareButtonAction&&StCompareButtonAction(),hoverimagedir())}function responsivecolumn(){$(document).width()<=991?($(".container #columns_inner #left-column").appendTo(".container #columns_inner"),$(window).bind("scroll",(function(){$(window).scrollTop()>200?$(".header-top").addClass("fixed"):$(".header-top").removeClass("fixed")}))):$(document).width()>=992&&($(".container #columns_inner #left-column").prependTo(".container #columns_inner"),$(window).bind("scroll",(function(){$(window).scrollTop()>215?$(".header-top").addClass("fixed"):$(".header-top").removeClass("fixed")}))),$("#language-selector").appendTo(".user-info > ul.dropdown-menu"),$("#currency-selector").appendTo(".user-info > ul.dropdown-menu")}czcategoryimagelist.owlCarousel({items:6,itemsDesktop:[1199,5],itemsDesktopSmall:[991,4],itemsTablet:[650,3],itemsTabletSmall:[480,2],itemsMobile:[320,1],autoPlay:!1}),$(".cat_next").click((function(){czcategoryimagelist.trigger("owl.next")})),$(".cat_prev").click((function(){czcategoryimagelist.trigger("owl.prev")})),$(document).ready((function(){responsivecolumn()})),$(window).resize((function(){responsivecolumn()}));