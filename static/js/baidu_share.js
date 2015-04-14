/**
 * Created by wushengyu on 15/4/3.
 */
function baidu_share(text, keywords) {
    window._bd_share_config = {
        "common": {
            "bdSnsKey": {},
            "bdText": text,
            "bdMini": "1",
            "bdDesc": keywords,
            "bdMiniList": ["mshare", "qzone", "tsina", "weixin", "renren", "tqq", "douban", "sqq", "isohu", "ty", "fbook", "twi", "linkedin", "copy"],
            "bdPic": "http://shadowwood.me/img/1.ico",
            "bdStyle": "1",
            "bdSize": "32"
        }, "slide": {"type": "slide", "bdImg": "1", "bdPos": "right", "bdTop": "30"}
    };
    with (document)0[(getElementsByTagName('head')[0] || body).appendChild(createElement('script')).src = 'http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion=' + ~(-new Date() / 36e5)];
}
