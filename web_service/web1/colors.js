
var Links = {
    setColor: function (color) {
        // var list = document.getElementsByClassName('list');
        // i = 0;
        // while (i < list.length) {
        //     list[i].style.color = color;
        //     i = i + 1;
        // };
        $('.list').css('color', color); // #으로 id, .으로 class, 대괄호[]로 name으로 list 불러옴. css 메서드로 'color' 속성 수정, 매개변수 color로 인자받음.
    }
}
var Body = {
    setColor: function (color) {
        // document.querySelector('body').style.color = color;
        $('body').css('color', color);
    },
    setBackgroundColor: function (color) {
        // document.querySelector('body').style.backgroundColor = color;
        $('body').css('backgroundColor', color);
    }
}
function nightDayHandler(self) {
    var target = document.querySelector('body');
    if (self.value === 'night') {
        Links.setColor('powderblue')
        Body.setBackgroundColor('black');
        Body.setColor('white');
        self.value = 'day'
    } else {
        Links.setColor('blue')
        Body.setBackgroundColor('white');
        Body.setColor('black')
        self.value = 'night'
    }
}