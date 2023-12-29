/*========================================== MASTER JAVASCRIPT ===================================================================

	Project     :	STARTUP TEMPLATES
	Version     :	1.0
	Last Change : 	04/05/2018
	Primary Use :   STARTUP TEMPLATES

=================================================================================================================================*/

$(document).on('ready', function() {
    "use strict"; //Start of Use Strict
    var menu_bar = $('.navbar-expand-lg');
    var menu_li = $('.navbar-nav li a');
    var collapse = $('.navbar-collapse');   
    var top_nav = $('#top-nav');
    var top_menu = $('.header-menu-1');

    //MENU-1 SCROLL
    if (top_menu.length) {
        var x = $(".header-menu-1").offset().top;
        var topx = (x - $(window).scrollTop());
        if (topx < 90) {

            menu_bar.fadeIn().addClass('fixed-header').css({
                "background-color": "#ffffff",
                "color": "#333333"
            });
            menu_li.css({
                "color": "#333333"
            });
			$(".logo-image").find('img').attr('src','images/150x50.png');
			
			
        } else {			
            menu_bar.removeClass('fixed-header').css({
                "background-color": "transparent",
                "color": "#ffffff"
            });
            menu_li.css({
                "color": "#ffffff"
            });
			$(".logo-image").find('img').attr('src','images/150x50x1.png');
        }
        $(document).on('scroll', function() {
            var y = $(window).scrollTop();

            if (y >= 90) {
                menu_bar.fadeIn().addClass('fixed-header').css({
                    "background-color": "#ffffff",
                    "color": "#333333"
                });
                menu_li.css({
                    "color": "#333333"
                });
				$(".logo-image").find('img').attr('src','images/150x50.png');

            } else {				
                menu_bar.removeClass('fixed-header').css({
                    "background-color": "transparent",
                    "color": "#ffffff"
                });
                menu_li.css({
                    "color": "#ffffff"
                });
				$(".logo-image").find('img').attr('src','images/150x50x1.png');
            }
        });
    }

    //MENU-2 SCROLL
    if (top_nav.length) {
        var x = top_nav.offset().top;
        if (x > 50) {
            top_nav.fadeIn();
        } else {
            top_nav.fadeOut();
        }
        $(document).on('scroll', function() {
            var y = $(this).scrollTop();
            if (y > 50) {
                top_nav.fadeIn();
            } else {
                top_nav.fadeOut();
            }
        });
    }

    //RESPONSIVE MENU SHOW AND HIDE FUNCTION
    if (menu_li.length) {
        menu_li.on("click", function(event) {
            collapse.slideToggle();
        });
        $('.navbar-expand-lg .navbar-toggler').on("click", function(e) {
            collapse.slideToggle();
        });
    }
	

    //MENU BAR SMOOTH SCROLLING FUNCTION
    var menu_list = $('.navbar-nav');
    if (menu_list.length) {
        menu_list.on("click", ".pagescroll", function(event) {
            event.stopPropagation();
            event.preventDefault();
            var hash_tag = $(this).attr('href');
            if ($(hash_tag).length) {
                $('html, body').animate({
                    scrollTop: $(hash_tag).offset().top - 50
                }, 2000);
            }
            return false;
        });
    }

    //COUNTER
    var counter = $('.count');
    if (counter.length) {
        counter.counterUp({
            delay: 10,
            time: 1000
        });
    }

    //GALLERY POPUP
    var gallery = $('.popup-gallery');
    if (gallery.length) {
        $('.popup-gallery').magnificPopup({
            delegate: 'a',
            type: 'image',
            tLoading: 'Loading image #%curr%...',
            mainClass: 'mfp-img-mobile',
            gallery: {
                enabled: true,
                navigateByImgClick: true,
                preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
            },
            image: {
                tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
                titleSrc: function(item) {
                    return item.el.attr('title') + '<small>by Marsel Van Oosten</small>';
                }
            }
        });
    }

    //VIDEO POPUP
    var video = $('.popup-youtube');
    if (video.length) {
        $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false
        });
    }

    //CONTACT FORM VALIDATION	
    if ($('.contact-form-1').length) {
        $('.contact-form-1').each(function() {
            $(this).validate({
                errorClass: 'error',
                submitHandler: function(form) {
                    $.ajax({
                        type: "POST",
                        url: "mail/mail.php",
                        data: $(form).serialize(),
                        success: function(data) {
                            if (data) {
                                $('.sucessMessage').html('Mail Sent Successfully !');
                                $('.sucessMessage').show();
                                $('.sucessMessage').delay(3000).fadeOut();
                            } else {
                                $('.failMessage').html(data);
                                $('.failMessage').show();
                                $('.failMessage').delay(3000).fadeOut();
                            }
                        },
                        error: function(XMLHttpRequest, textStatus, errorThrown) {
                            $('.failMessage').html(textStatus);
                            $('.failMessage').show();
                            $('.failMessage').delay(3000).fadeOut();
                        }
                    });
                }
            });
        });
    }

    // YOUTUBE BACKGROUND VIDEO FUNCTION	
    var player = $('.player');
    if (player.length) {
        player.mb_YTPlayer();
    }
	
    //FAQ ACCORDION
	var accordion = $(".faq-row");
    if (accordion.length) {
        accordion.each(function() {
            var all_panels = $(this).find('.faq-ans').hide();
            var all_titles = $(this).find('.faq-title');
            $(this).find('.faq-ans.active').slideDown();

            all_titles.on("click", function() {
                var acc_title = $(this);
                var acc_inner = acc_title.next();

                if (!acc_inner.hasClass('active')) {
                    all_panels.removeClass('active').slideUp();
                    acc_inner.addClass('active').slideDown();
                    all_titles.removeClass('active');
                    acc_title.addClass('active');
                } else {
                    all_panels.removeClass('active').slideUp();
                    all_titles.removeClass('active');
                }
            });
        }); 
        $(".faq-row .faq-div:first-child .faq-ans").css("display", "block");
    }
	
	//PRICE TABLE
	var carousel = $(".carousel-div");
	if (carousel.length) {
		var carousel = $(".carousel-div"),
		currdeg = 0;       
		
		var rotate = function(e){
		  if(e.data.d=="n"){
			currdeg = currdeg - 60;
		  }
		  if(e.data.d=="p"){
			currdeg = currdeg + 60;
		  }
		  carousel.css({
			"-webkit-transform": "rotateY("+currdeg+"deg)",
			"-moz-transform": "rotateY("+currdeg+"deg)",
			"-o-transform": "rotateY("+currdeg+"deg)",
			"transform": "rotateY("+currdeg+"deg)"	
		  });
		}
		$(".next").on("click", { d: "n" }, rotate);
		$(".prev").on("click", { d: "p" }, rotate);
		
	}
    return false;
    // End of use strict
});