/**
 * Created by wushengyu on 15/4/3.
 */
function to_somewhere(position){
    $("html, body").animate({scrollTop: $(position).offset().top}, 1000);
}