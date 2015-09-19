/**
 * Created by wushengyu on 15/4/18.
 */

function add_new_comment(){
    if($('#comment_name').val() && $('#comment_content').val()){
        if($('#comment_name').val() == "</Shadow>" && !$('#author_if').val()){
            $('#comment_warning').text('请不要冒充博主0.0').show();
            return false
        }
        if($('#comment_e_mail').val()){
            var is_email= /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
            if(is_email.test($('#comment_e_mail').val())){
                $('#comment_form').submit();
            }
            else{
                $('#comment_warning').text('请输入正确的邮箱').show();
            }
        }
        else{
            $('#comment_form').submit();
        }
    }
    else{
        $('#comment_warning').text("请完善需要提交的信息").show();
    }
}

function add_new_reply(){
    if($('#reply_name').val() && $('#reply_content').val()){
        if($('#reply_name').val() == "</Shadow>" && !$('#author_if').val()){
            $('#reply_warning').text('请不要冒充博主0.0').show();
            return false
        }
        if($('#reply_e_mail').val()){
            var is_email= /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
            if(is_email.test($('#reply_e_mail').val())){
                $('#reply_form').submit();
            }
            else{
                $('#reply_warning').text('请输入正确的邮箱').show();
            }
        }
        else{
            $('#reply_form').submit();
        }
    }
    else{
        $('#reply_warning').text("请完善需要提交的信息").show();
    }
}

function hidden_reply(){
    $('#reply_panel').fadeOut("1500");
    $('#to_comment_id').val('')
}

function add_reply_form(comment_id, reply_name, div_id){
    if($('#to_comment_id').val() == comment_id){
        return true
    }
    var add_Html = $('#reply_panel').html();
    console.log(add_Html);
    $('#reply_panel').remove();
    $('#'+div_id).append("<div id='reply_panel' class='col-lg-12 col-md-12 col-sm-12 col-xs-12' style='display: none;margin-top: 2px;padding: 0;'></div>");
    $('#reply_panel').append(add_Html);
    if(reply_name){
        $('#to_reply_name').val(reply_name);
    }
    else{
        $('#to_reply_name').val('');
    }
    $('#to_comment_id').val(comment_id);
    $('#reply_panel').fadeIn("1500")
}

function delete_comment(article_id, comment_id){
    $.ajax({
        type: 'POST',
        url: 'delete_comment',
        data: {'article_id': article_id,
               'comment_id': comment_id,
               'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val()},
        success: function(data){
            if(data == 'T'){
                $('#comment-reply-' + comment_id).remove();
            }
            else{
                alert("操作失败")
            }
        }
    })
}

function delete_reply(article_id, comment_id, reply_id){
    $.ajax({
        type: 'POST',
        url: 'delete_reply',
        data: {'article_id': article_id,
               'comment_id': comment_id,
               'reply_id': reply_id,
               'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val()},
        success: function(data){
            if(data == 'T'){
                $('#reply-' + reply_id).remove();
            }
            else{
                alert("操作失败")
            }
        }
    })
}

function delete_article(article_id, type_name){
    $.ajax({
        type: 'POST',
        url: 'delete_article',
        data: {'article_id': article_id,
               'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val()},
        success: function(data){
            if(data == 'T'){
                window.location.href = "/blog_list?type_name=" + type_name;
            }
            else{
                alert("操作失败")
            }
        }
    })
}