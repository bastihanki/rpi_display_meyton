function pageScroll() {
    const waitBefore = 4000;
    const waitAfter = 4000;
    const step = 1;
    const speed = 50;
    function scroll() {
        var position = window.pageYOffset;
        window.scrollBy(0, step);
        if (position === window.pageYOffset) {
            setTimeout(function () {
                window.location = "xxx";
            }, waitAfter);
        } else {
            window.setTimeout(scroll, speed);
        }
    }
    setTimeout(scroll, waitBefore);
}