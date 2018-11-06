$(function () {
    $('.register').width(innerWidth)

    // 账号验证
    $('#account input').blur(function () {
        // 数字、字母
        var reg = /^[A-Za-z0-9]+$/
        if(reg.test($(this).val())){ // 符合
            $('#account i').html('')
            $('#account').removeClass('has-error').addClass('has-success')
            $('#account span').addClass('glyphicon-ok')
        }else{ // 不符合
            $('#account i').html('账号由数字或字母组成')
            $('#account').addClass('has-error')
            $('#account span').removeClass('has-success').addClass('glyphicon-remove')
        }
    })

     // 密码验证
    $('#password input').blur(function () {
        // if($(this).val() == '') return
        // 数字.
        var reg = /^[\d]{6,12}$/
        if(reg.test($(this).val()) ){ // 符合
            $('#password i').html('')
            $('#password').removeClass('has-error').addClass('has-success')
            $('#password span').addClass('glyphicon-ok')
        }else{ // 不符合
            $('#password i').html('6~12位纯数字')
            $('#password').addClass('has-error')
            $('#password span').removeClass('has-success').addClass('glyphicon-remove')
        }
    })
})