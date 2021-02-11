$(function () {
    $('.burger').click(function () {
        $('.main-menu').addClass('d-block');
        $('.overlay').show();
    });
    $('.overlay').click(function () {
        $('.main-menu').removeClass('d-block');
        $('.overlay').hide();
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
    const tech = $('#techCarousel .carousel-item').get(0)
    if (tech) {
        tech.classList.add('active')
    }
    const concreting = $('#concretingCarousel .carousel-item').get(0)
    if (concreting) {
        concreting.classList.add('active')
    }
    const persons = $('#personsCarousel .carousel-item').get(0)
    if(persons) {
        persons.classList.add('active')
    }
    const activity = $('#activityCarousel .carousel-item').get(0)
    if(activity) {
        activity.classList.add('active')
    }
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
                }).then($('#form_add_resume').trigger('reset')):
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
                }).then($('#form_add_order').trigger('reset')):
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