$(function () {
    $('.market').width(innerWidth)

    // 获取typeIndex
    typeIndex = $.cookie('typeIndex')
    if (typeIndex){ // 已经有点击分类
        $('.type-slider .type-item').eq(typeIndex).addClass('active')
    }else{ // 没有点击分类
        $('.type-slider .type-item:first').addClass('active')
    }

    // 侧边栏
    // cookie
    // 设置cookie
    // $.(key,value,options)    options  >  {expires:过期时间,path:路径}
    // 获取cookie
    // 删除cookie
    $('.type-item').click(function () {
        // $(this).addClass('active')
        // 设置cookie
        $.cookie('typeIndex',$(this).index(),{expires:3,path:'/'})

    })
})