$(function () {
    $('.burger').click(function () {
        if ($('.main-menu').hasClass("showed_menu")) {
            $('.main-menu').removeClass('showed_menu')
            $('.main-menu').slideUp();
            $('.overlay').hide();
        } else {
            $('.main-menu').addClass('showed_menu')
            $('.main-menu').slideDown();
            $('.overlay').show();
        }
    });
    $('.overlay').click(function () {
        $('.main-menu').removeClass('showed_menu')
        $('.main-menu').slideUp();
        $('.overlay').hide();
    });
    $('.with-submenu').click(function () {
        $(this).next('.main-submenu').slideToggle();
    });

    $('.projects-carousel').slick({
        slidesToShow: 4,
        // arrows: false,
        appendArrows: $(".projects-arrows"),
        prevArrow: '<a href="#" class="arrow left"></a>',
        nextArrow: '<a href="#" class="arrow right ml-4"></a>',
        responsive: [
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 3,
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                }
            },
            {
                breakpoint: 576,
                settings: {
                    slidesToShow: 1,
                }
            }
        ]
    });
});

$("#form_AdviseFree").on("submit", function (e) {
    e.preventDefault();
    let t = $(this), o = t.serializeArray();
    $.ajax({
        url: t.attr("action"), type: t.attr("method"), data: o, dataType: "json", success: function (e) {
            e.status ? Swal.fire({
                    icon: "success",
                    html: e.message,
                    timer: 1000,
                    timerProgressBar: true,
                    showConfirmButton: false
                }).then($('#form_AdviseFree').trigger('reset')) :
                Swal.fire({
                    icon: 'error',
                    html: e.message,
                    timer: 1000,
                    timerProgressBar: true,
                    showConfirmButton: false
                })
            console.log(e.form)
        }
    })
})
$("#form_add_resume").on("submit", function (e) {
    e.preventDefault();
    let t = $(this), o = t.serializeArray();
    $.ajax({
        url: t.attr("action"), type: t.attr("method"), data: o, dataType: "json", success: function (e) {
            e.status ? Swal.fire({
                    icon: "success",
                    html: e.message,
                    timer: 1000,
                    timerProgressBar: true,
                    showConfirmButton: false
                }).then($('#form_add_resume').trigger('reset')) :
                Swal.fire({
                    icon: 'error',
                    html: e.message,
                    timer: 1000,
                    timerProgressBar: true,
                    showConfirmButton: false
                })
        }
    })
})

$("#form_add_order").on("submit", function (e) {
    e.preventDefault();
    let t = $(this), o = t.serializeArray();
    $.ajax({
        url: t.attr("action"), type: t.attr("method"), data: o, dataType: "json", success: function (e) {
            e.status ? Swal.fire({
                    icon: "success",
                    html: e.message,
                    timer: 1000,
                    timerProgressBar: true,
                    showConfirmButton: false
                }).then($('#form_add_order').trigger('reset')) :
                Swal.fire({
                    icon: 'error',
                    html: e.message,
                    timer: 1000,
                    timerProgressBar: true,
                    showConfirmButton: false
                })
        }
    })
})

$("#form_add_order_object").on("submit", function (e) {
    e.preventDefault();
    let t = $(this), o = t.serializeArray();
    $.ajax({
        url: t.attr("action"), type: t.attr("method"), data: o, dataType: "json", success: function (e) {
            e.status ? Swal.fire({
                    icon: "success",
                    html: e.message,
                    timer: 1000,
                    timerProgressBar: true,
                    showConfirmButton: false
                }).then($('#form_add_order_object').trigger('reset')) :
                Swal.fire({
                    icon: 'error',
                    html: e.message,
                    timer: 1000,
                    timerProgressBar: true,
                    showConfirmButton: false
                })
        }
    })
})

$("body").on('click', '[href*="#"]', function(e){
    var fixed_offset = 100;
    $('html,body').stop().animate({ scrollTop: $(this.hash).offset().top - fixed_offset }, 1000);
    e.preventDefault();
  });
const btn_on_top = document.querySelector(".btn_on_top")
const  trackScroll=()=> {
    let scrolled = window.pageYOffset;
    let coords = document.documentElement.clientHeight;

    if (scrolled > coords) {
        btn_on_top.classList.remove('d-none');
    }
    if (scrolled < coords) {
        btn_on_top.classList.add('d-none');
    }
}
window.addEventListener('scroll', trackScroll);