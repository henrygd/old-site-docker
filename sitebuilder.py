

def build(styles, logo, background, orgfont, showfont, bodyfont, butthov, logocolor,
           barcolor, buttoncolor, navbartext, stripepk, introtextcolor, aboutback,
           eventsback, contactback, contacticons, linkcolor, mapcoords, twitter,
           facebook, youtube, orgname, navabout, navevents, navcontact, introtext,
           abouthead, aboutsub, aboutcont, eventhead, contacthead, phone, address,
           mandrill_api, email, eventstatus, mapstatus, cal_api, cal_id):

    if eventstatus == 'false':
        events, navbarevents, calendar, calendarevents, gcalscript = '', '', '', '', ''
    else:
        navbarevents = """<li id="eventnav"><a class="page-scroll" href="#events">%s</a></li>""" % (navevents)

        calendar = """<link href="https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.2.3/fullcalendar.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.2.3/fullcalendar.print.css" rel="stylesheet" media='print'>
        <script src='https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.8.3/moment.min.js'></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/2.2.3/fullcalendar.min.js"></script>"""

        events = """\n\n<!-- Events Section -->
        <section id="events">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12 text-center">
                        <div class="section-heading">%s</div>
                    </div>
                <div class="row">
                    <div class="col-lg-12">
                        <div id='calendar'></div>
                    </div>
                </div>
                </div>
            </div>
        </section>\n\n""" % (eventhead)

        calendarevents = """\n<!-- calendar events -->
        <script>
        $(document).ready(function() {
            $('#calendar').fullCalendar({
                googleCalendarApiKey: '%s',
                header:{left:"prev,next today",center:"title",right:"month,basicWeek"},
                eventLimit:true,
                height:520,
                events: {
                    googleCalendarId: '%s',
                },
                eventClick: function(event) {
                if (event.url) {
                    window.open(event.url);
                    return false;
                }
            }
            });
        });
    </script>\n""" % (cal_api, cal_id)

        gcalscript = """<script>(function(e){if(typeof define==="function"&&define.amd){define(["jquery"],e)}else{e(jQuery)}})(function(e){function i(n,i,o,u,a){function d(t,r){var i=r||[{message:t}];var s=window.console;var o=s?s.warn||s.log:null;(n.googleCalendarError||e.noop).apply(a,i);(a.options.googleCalendarError||e.noop).apply(a,i);if(o){o.apply(s,[t].concat(r||[]))}}var f=t+"/"+encodeURIComponent(n.googleCalendarId)+"/events?callback=?";var l=n.googleCalendarApiKey||a.options.googleCalendarApiKey;var c=n.success;var h;var p;if(!l){d("Specify a googleCalendarApiKey. See http://fullcalendar.io/docs/google_calendar/");return{}}if(!i.hasZone()){i=i.clone().utc().add(-1,"day")}if(!o.hasZone()){o=o.clone().utc().add(1,"day")}if(u&&u!="local"){p=u.replace(" ","_")}h=e.extend({},n.data||{},{key:l,timeMin:i.format(),timeMax:o.format(),timeZone:p,singleEvents:true,maxResults:9999});return e.extend({},n,{googleCalendarId:null,url:f,data:h,startParam:false,endParam:false,timezoneParam:false,success:function(t){var n=[];var i;var o;if(t.error){d("Google Calendar API: "+t.error.message,t.error.errors)}else if(t.items){e.each(t.items,function(e,t){var r=t.htmlLink;if(p){r=s(r,"ctz="+p)}n.push({id:t.id,title:t.summary,start:t.start.dateTime||t.start.date,end:t.end.dateTime||t.end.date,url:r,location:t.location,description:t.description})});i=[n].concat(Array.prototype.slice.call(arguments,1));o=r(c,this,i);if(e.isArray(o)){return o}}return n}})}function s(e,t){return e.replace(/(\?.*?)?(#|$)/,function(e,n,r){return(n?n+"&":"?")+t+r})}var t="https://www.googleapis.com/calendar/v3/calendars";var n=e.fullCalendar;var r=n.applyAll;n.sourceNormalizers.push(function(e){var t=e.googleCalendarId;var n=e.url;var r;if(!t&&n){if(r=/^[^\/]+@([^\/\.]+\.)*(google|googlemail|gmail)\.com$/.test(n)){t=n}else if((r=/^https:\/\/www.googleapis.com\/calendar\/v3\/calendars\/([^\/]*)/.exec(n))||(r=/^https?:\/\/www.google.com\/calendar\/feeds\/([^\/]*)/.exec(n))){t=decodeURIComponent(r[1])}if(t){e.googleCalendarId=t}}if(t){if(e.editable==null){e.editable=false}e.url=t}});n.sourceFetchers.push(function(e,t,n,r){if(e.googleCalendarId){return i(e,t,n,r,this)}})})</script>"""

    if mapstatus == 'false':
        map1, map2 = '', ''
    else:
        map1 = """<section id="map"></section>"""
        map2 = """\n\t<!-- map -->
        <script src="https://maps.googleapis.com/maps/api/js?v=3"></script>
        <script>
            function init(){var e=new google.maps.LatLng(%s);var t={zoom:13,center:e};var n=document.getElementById("map");var r=new google.maps.Map(n,t);var i=new google.maps.Marker({position:e,map:r})}google.maps.event.addDomListener(window,"load",init)
        </script>""" % (mapcoords)

    if background is None:
        backstretch1, backstretch2 = '', ''
    else:
        if 'https' in background:
            backstretch1 = """\n\t<!-- background, based on Backstretch v2.0.4-->\n\t<script>!function(t,i,e){t.fn.backstretch=function(n,s){return(n===e||0===n.length)&&t.error("No images were supplied for Backstretch"),0===t(i).scrollTop()&&i.scrollTo(0,0),this.each(function(){var i=t(this),e=i.data("backstretch");if(e){if("string"==typeof n&&"function"==typeof e[n])return void e[n](s);s=t.extend(e.options,s),e.destroy(!0)}e=new r(this,n,s),i.data("backstretch",e)})},t.backstretch=function(i,e){return t("body").backstretch(i,e).data("backstretch")},t.expr[":"].backstretch=function(i){return t(i).data("backstretch")!==e},t.fn.backstretch.defaults={centeredX:!0,centeredY:!0,duration:5e3,fade:0};var n={left:0,top:0,overflow:"hidden",margin:0,padding:0,height:"100%",width:"100%",zIndex:-999999},s={position:"absolute",display:"none",margin:0,padding:0,border:"none",width:"auto",height:"auto",maxHeight:"none",maxWidth:"none",zIndex:-999999},r=function(e,s,r){this.options=t.extend({},t.fn.backstretch.defaults,r||{}),this.images=t.isArray(s)?s:[s],t.each(this.images,function(){t("<img />")[0].src=this}),this.isBody=e===document.body,this.$container=t(e),this.$root=this.isBody?t(o?i:document):this.$container,e=this.$container.children(".backstretch").first(),this.$wrap=e.length?e:t('<div class="backstretch"></div>').css(n).appendTo(this.$container),this.isBody||(e=this.$container.css("position"),s=this.$container.css("zIndex"),this.$container.css({position:"static"===e?"relative":e,zIndex:"auto"===s?0:s,background:"none"}),this.$wrap.css({zIndex:-999998})),this.$wrap.css({position:this.isBody&&o?"fixed":"absolute"}),this.index=0,this.show(this.index),t(i).on("resize.backstretch",t.proxy(this.resize,this)).on("orientationchange.backstretch",t.proxy(function(){this.isBody&&0===i.pageYOffset&&(i.scrollTo(0,1),this.resize())},this))};r.prototype={resize:function(){try{var t={left:0,top:0},i=this.isBody?this.$root.width():this.$root.innerWidth(),e=i,n=(navigator.userAgent.match(/(iPad|iPod|iPhone|Android)/)?100:0)+(this.isBody?window.innerHeight?window.innerHeight:this.$root.height():this.$root.innerHeight());j=e/this.$img.data("ratio"),j>=n?(a=(j-n)/2,this.options.centeredY&&(t.top="-"+a+"px")):(j=n,e=j*this.$img.data("ratio"),a=(e-i)/2,this.options.centeredX&&(t.left="-"+a+"px")),this.$wrap.css({width:i,height:n}).find("img:not(.deleteable)").css({width:e,height:j}).css(t)}catch(s){}return this},show:function(i){if(!(Math.abs(i)>this.images.length-1)){var e=this,n=e.$wrap.find("img").addClass("deleteable"),r={relatedTarget:e.$container[0]};return e.$container.trigger(t.Event("backstretch.before",r),[e,i]),this.index=i,clearInterval(e.interval),e.$img=t("<img />").css(s).bind("load",function(s){var o=this.width||t(s.target).width();s=this.height||t(s.target).height(),t(this).data("ratio",o/s),t(this).fadeIn(e.options.speed||e.options.fade,function(){n.remove(),e.paused||e.cycle(),t(["after","show"]).each(function(){e.$container.trigger(t.Event("backstretch."+this,r),[e,i])})}),e.resize()}).appendTo(e.$wrap),e.$img.attr("src",e.images[i]),e}},next:function(){return this.show(this.index<this.images.length-1?this.index+1:0)},prev:function(){return this.show(0===this.index?this.images.length-1:this.index-1)},pause:function(){return this.paused=!0,this},resume:function(){return this.paused=!1,this.next(),this},cycle:function(){return 1<this.images.length&&(clearInterval(this.interval),this.interval=setInterval(t.proxy(function(){this.paused||this.next()},this),this.options.duration)),this},destroy:function(e){t(i).off("resize.backstretch orientationchange.backstretch"),clearInterval(this.interval),e||this.$wrap.remove(),this.$container.removeData("backstretch")}};var o,a=navigator.userAgent,h=navigator.platform,c=a.match(/AppleWebKit\/([0-9]+)/),c=!!c&&c[1],d=a.match(/Fennec\/([0-9]+)/),d=!!d&&d[1],p=a.match(/Opera Mobi\/([0-9]+)/),f=!!p&&p[1],g=a.match(/MSIE ([0-9]+)/),g=!!g&&g[1];o=!((-1<h.indexOf("iPhone")||-1<h.indexOf("iPad")||-1<h.indexOf("iPod"))&&c&&534>c||i.operamini&&"[object OperaMini]"==={}.toString.call(i.operamini)||p&&7458>f||-1<a.indexOf("Android")&&c&&533>c||d&&6>d||"palmGetResource"in i&&c&&534>c||-1<a.indexOf("MeeGo")&&-1<a.indexOf("NokiaBrowser/8.5.0")||g&&6>=g)}(jQuery,window);</script>"""
            backstretch2 = """<script>$.backstretch("%s");</script>\n""" % (background)
            background = ''
        else:
            backstretch1, backstretch2 = '', ''

    if facebook == '':
        facebooklink = ''
    else:
        facebooklink = """<li id="facebook"><a href="%s" target="_blank"><i class="fa fa-facebook-square" ></i></a></li>""" % (facebook)

    if youtube == '':
        youtubelink = ''
    else:
        youtubelink = """<li id="youtube"><a href="%s" target="_blank"><i class="fa fa-youtube-square"></i></a></li>""" % (youtube)

    if twitter == '':
        twitterlink = ''
    else:
        twitterlink = """<li id="twitter"><a href="%s" target="_blank"><i class="fa fa-twitter-square"></i></a></li>""" % (twitter)

    if bodyfont[66:71] == orgfont[65:70] or showfont[66:71] == orgfont[65:70]:
        orgfont = ""

    if bodyfont[66:71] == showfont[66:71]:
        bodyfont = ""

    style = "body{height:100%%;width:100%%;overflow-x:hidden;font-size:15px%s}.intro-heading>h1{font-size:50px}.btny{border:none;font-family:inherit;font-size:inherit;color:inherit;background:none;cursor:pointer;padding:15px 10px;display:inline-block;text-transform:uppercase;letter-spacing:1px;font-weight:700;outline:none;position:relative;-webkit-transition:all .3s;-moz-transition:all .3s;transition:all .3s;font-size:16px;min-width: 90px;font-family:Montserrat,'Helvetica Neue'}.btn-2,.social-buttons{text-shadow:0px 1px 1px rgba(0,0,0,0.3)}.btn-2{background:%s;color:#fff;border-radius:5px;-webkit-transition:none;-moz-transition:none;transition:none}.donatebutton{font-size:13px!important;padding:7px 13px!important;background-color:#7B79CA!important;box-shadow:0 4px #5458AE!important}.donatebutton:hover{box-shadow:0 5px #5458AE!important;top:-1px}.donatebutton:active{box-shadow:none!important;}#DonateModal input:focus{border:none}#DonateModal input{color:#C7C7C7;background-color:#4F4F4F;border:none;font-size:18px;height:37px}#DonateModal .modal-content,#ThanksModal .modal-content{border-radius:0;background:rgba(207,207,207,.8);color:#797979}#DonateModal .input-group-addon{padding:3px 8px;background:#676767;color:#BDBDBD;border:none}#DonateModal .modal-header,#ThanksModal .modal-header{padding:0;height:25px;border-bottom:none}#DonateModal .modal-header .close,#ThanksModal .modal-header .close{margin:0;padding:5px}#DonateModal .modal-footer,#ThanksModal .modal-footer{padding:3px 9px 17px;text-align:center}#ThanksModal .modal-body{color:#444;text-align:center;padding:40px 40px}#bicon{color:%s}.intro-heading{color:%s}#about{%s}#events{%s}#contact{%s;padding-bottom:0}.contactboxes i{color:%s}.navbar-shrink,.navbar-default .navbar-toggle .icon-bar{background:%s}.navbar-brand,.nav li a,.navbar-default .navbar-nav > .active > a{color:%s!important}.navbar-default .navbar-toggle{background-color:%s;border:none;padding:6px 4px;margin-top:11px}#about a{color:%s}a.fc-more{color:#fff}[id$='Modal']{z-index:99991}.modal-footer{padding:8px;clear:both}#map{height:400px}#calendar{width:98%%;margin:auto}.fc-view-container{font-size:1.1em;box-shadow:0px 0px 55px rgba(0,0,0,0.6)}.fc-center>h2{color:#fafafa}.fc td,.fc th{border:1px solid #675431}.fc td{background:rgba(45,45,45,.6);color:wheat}.fc-unthemed .fc-today{background:rgba(107,107,107,.55)}.fc-event{background-color:#907A52;border:none;border-radius:0}.fc a:visited{color:#fafafa;text-decoration:none}.fc button{border-radius:0!important}.fc-unthemed .fc-popover{background-color:#4C4C4C;border:none}.fc-unthemed .fc-popover .fc-header{padding:1px;background:#626262}.fc-unthemed .fc-popover .fc-header .fc-close{color:#CFCFCF;margin-top:8px}#calendar{width:98%%;margin:auto}#contact .container{margin-top:-12px}#contact .section-heading h2{color:#EEE;margin-bottom:0}footer{text-align:center;background:rgba(255,255,255,0.82);padding:20px 0 15px;box-shadow:0 1px 5px rgba(0,0,0,0.39)}footer span.copyright{line-height:40px}footer a.quicklink{margin-bottom:0;line-height:40px}ul.social-buttons{margin:0;}ul.social-buttons li a{display:block;font-size:2.6em;line-height:40px;color:#222;-webkit-transition:all .2s;-moz-transition:all .2s;transition:all .2s}#twitter a:hover{color:#13BABB}#facebook a:hover{color:#3B5999}#youtube a:hover{color:#FF2424}#events .section-heading h2{color:#fafafa}.contactboxes{color:#fff}.fa-home{font-size:40px!important;margin:5px 0 14px}.fa-envelope,.fa-phone{font-size:34px!important;margin:20px 0 14px}.contactboxes div>p{line-height:.7}*[id^='box-']{height:160px;padding: 30px 0 40px;}.contactboxes #box-1{background-color:rgba(40, 40, 40, 0.7)}.contactboxes #box-2{background-color:rgba(32, 32, 32, 0.7)}.contactboxes #box-3{background-color:rgba(24, 24, 24, 0.7)}.text-muted{color:#777}.text-primary{color:#fed136}p{line-height:1.55}p.large{font-size:16px}.btn-primary{color:#fff;border:none;background-color:#fed136}.navbar-default{border-color:transparent;box-shadow:0 1px 5px rgba(0,0,0,0.39);%s}.navbar-default .navbar-collapse{border-color:rgba(255,255,255,.02)}.navbar-default .navbar-toggle .icon-bar{background-color:%s}.navbar-default .nav li a{font-weight:700;letter-spacing:1px;color:#E43434}.navbar-default .navbar-nav > .active > a:hover,.navbar-default .navbar-nav>.active>a,.navbar-default .nav li a:hover,.navbar-default .nav li a:focus{outline:0;color:#E43434}header{text-align:center;color:#fff;background:none}header .intro-text{padding-top:120px;padding-bottom:70px}header .intro-text .intro-heading{margin-bottom:25px;font-size:50px;line-height:50px}.container{max-width:95%%;}section{padding:80px 0 100px;width:97%%;max-width: 1470px; margin: 0 auto;box-shadow:0px 0px 24px rgba(0,0,0,0.5);margin-bottom:15px}section .section-heading h2{margin-top:0;margin-bottom:15px;font-size:40px;text-shadow:0px 1px 2px rgba(0,0,0,0.3)}section#contact .form-group input.form-control{height:63px}section#contact .form-group textarea.form-control{height:220px}section#contact::-webkit-input-placeholder,section#contact:-moz-placeholder,section#contact::-moz-placeholder,section#contact:-ms-input-placeholder{text-transform:uppercase;font-weight:700;color:#bbb}section#contact p>ul{background:#EF5F5F;text-align:center;border-radius:3px;color:#F9F9F9;padding:2px 0 3px;font-size:16px}section#contact p>ul>li{list-style:none}.btn:focus,.btn:active,.btn.active,.btn:active:focus{outline:0}img::selection{background:0 0}img::-moz-selection{background:0 0}@media(min-width:768px){.fc-center{margin-left:-33px}header .intro-text{padding-top:290px;padding-bottom:180px}.intro-heading>h1{font-size: 75px;}header .intro-text .intro-heading{margin-bottom:50px;font-size:75px;line-height:75px}.btn-xl{padding:18px 30px;font-size:20px;transition:all 0.3s}#calendar{width:auto;margin:auto}.navbar-default{padding:10px 0;border:0;background:none;-webkit-transition:padding .3s;-moz-transition:padding .3s;transition:padding .3s;box-shadow:none}.navbar-default .navbar-brand{font-size:2em;padding:10px 15px;-webkit-transition:all .3s;-moz-transition:all .3s;transition:all .3s}.navbar-default.navbar-shrink{padding:0;box-shadow:0px 1px 5px rgba(0,0,0,0.39);%s}.navbar-default.navbar-shrink .navbar-brand{font-size:1.5em;padding-top:12px}*[id^='box-']{height:190px;padding:40px}.btny{font-size:19px;padding:18px 21px;min-width:140px;section{margin-bottom:30px}}}#loadingpin{display:none;position:fixed;left:50%%;top:45%%;z-index:9}#loading{display:none;position:absolute;color:#fafafa;left:-15px;top:-35px;}@media(max-width:580px){.fc-toolbar .fc-left{float: left;width:50%%;}.fc-toolbar .fc-left>*{float:right}.fc-toolbar .fc-right{float:right;width:50%%}.fc-toolbar .fc-right>*{float:left}.fc-toolbar .fc-center{width:100%%}.fc-center>h2{float:none!important;margin:10px 12%% 0 0}.fc .fc-toolbar>*>:first-child{margin-left:6%%}}@media(max-width:380px){.navbar-brand{font-size:17px;padding:13px 0 0 3px;height:auto}.navbar-default .navbar-toggle{padding:5px 3px;margin-top:13px}header .intro-text{padding:80px 0 60px}.intro-heading>h1{font-size:45px;word-wrap:normal}section{padding:60px 0}.fc-toolbar button{font-size:12px!important}.fc-more,.fc-time,.fc-title{font-size:10px!important}}" % (
        background, buttoncolor, logocolor, introtextcolor, aboutback, eventsback, contactback,
        contacticons, barcolor, navbartext, navbartext, linkcolor, barcolor, barcolor, barcolor)

    part1 = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>%s</title>

        <!-- Bootstrap Core CSS -->
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css" rel="stylesheet">

        <!-- Custom Fonts -->
        <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">
        %s%s%s
        <!-- jQuery / Plugins  -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
        %s
        %s

        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
            <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->

        <style>%s%s%s</style>
    </head>

    <body id="page-top">

        <!-- Navigation -->
        <nav class="navbar navbar-default navbar-fixed-top">
            <div class="container">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header page-scroll">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand page-scroll" href="#page-top"><span id="bicon" class="%s"></span>  %s</a>
                </div>

                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav navbar-right">
                        <li class="hidden">
                            <a href="#page-top"></a></li>
                        <li><a class="page-scroll" href="#about">%s</a></li>
                        %s
                        <li><a class="page-scroll" href="#contact">%s</a></li>
                    </ul>
                </div>
                <!-- /.navbar-collapse -->
            </div>
            <!-- /.container-fluid -->
        </nav>

        <!-- Header -->
        <header>
            <div class="container">
                <div class="intro-text">
                    <div class="intro-heading">%s</div>
                    <a href="#about" class="btny btn-2 page-scroll" style="color:#fff;text-decoration:none">Read More</a>
                </div>
            </div>
        </header>

        <!-- About Section -->
        <section id="about">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12 text-center">
                        <div class="section-heading">%s</div>
                        <h3 class="section-subheading text-muted">%s</h3>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-10 col-lg-offset-1">
                        <div>%s</div>
                    </div>
                </div>
            </div>
        </section>""" % (
        orgname, showfont, orgfont, bodyfont, calendar, gcalscript, style, styles, butthov,
        logo, orgname, navabout, navbarevents, navcontact, introtext, abouthead, aboutsub, aboutcont)

    part2 = """<!-- Contact Section -->
        <section id="contact" style="padding:0px">
            <div class="container-fluid">
              <div class="row contactboxes text-center">
                    <div class="col-md-4" id="box-1">
                        <i class="fa fa-phone"></i>
                            <p>%s</p>
                    </div>
                    <div class="col-md-4" id="box-2">
                        <i class="fa fa-home"></i>
                            %s
                    </div>
                    <div class="col-md-4" id="box-3">
                        <i class="fa fa-envelope"></i>
                            <p>%s</p>
                    </div>
                </div>
            </div>
        </section>

        %s

        <footer>
            <div class="container">
                <div class="row">
                    <div class="col-md-4">
                        <span class="copyright">Copyright &copy; %s 2015</span>
                    </div>
                    <div class="col-md-4">
                        <ul class="list-inline social-buttons">
                            %s
                            %s
                            %s
                        </ul>
                    </div>
                    <div class="col-md-4">
                        <a class="quicklink" target="_blank" href="https://henrygd.me/makeawebsite" style="color:#DA4A3E">Make your own nonprofit site free!</a>
                    </div>
                </div>
            </div>
        </footer>

        <!-- loading icon (fontawesome) -->
        <div id="loadingpin">
            <div id="loading"><i class="fa fa-spinner fa-3x fa-spin"></i></div>
        </div>

        <!-- Bootstrap JavaScript -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>

        <!-- Plugin JavaScript -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>

        <!-- ajax loading icon -->
        <script>
            $(document).bind("ajaxSend", function(){
              $("#resultinfo").html("");
              $("#loadingpin, #loading").show();
            }).bind("ajaxComplete", function(){
              $("#loadingpin, #loading").hide();
           });
        </script>

        %s
        %s
        %s
        <!-- classie -->
        <script>
            (function(e){"use strict";function t(e){return new RegExp("(^|\\s+)"+e+"(\\s+|$)")}function s(e,t){var s=n(e,t)?i:r;s(e,t)}var n,r,i;if("classList"in document.documentElement){n=function(e,t){return e.classList.contains(t)};r=function(e,t){e.classList.add(t)};i=function(e,t){e.classList.remove(t)}}else{n=function(e,n){return t(n).test(e.className)};r=function(e,t){if(!n(e,t)){e.className=e.className+" "+t}};i=function(e,n){e.className=e.className.replace(t(n)," ")}}var o={hasClass:n,addClass:r,removeClass:i,toggleClass:s,has:n,add:r,remove:i,toggle:s};if(typeof define==="function"&&define.amd){define(o)}else{e.classie=o}})(window)
        </script>

        <!-- animated navbar from codrops.com -->
        <script>
            var cbpAnimatedHeader=function(){function i(){window.addEventListener("scroll",function(e){if(!n){n=true;setTimeout(s,250)}},false)}function s(){var e=o();if(e>=r){classie.add(t,"navbar-shrink")}else{classie.remove(t,"navbar-shrink")}n=false}function o(){return window.pageYOffset||e.scrollTop}var e=document.documentElement,t=document.querySelector(".navbar-default"),n=false,r=100;i()}()
        </script>

        <!-- page scroll -->
        <script>
            $(function(){$("a.page-scroll").bind("click",function(e){var t=$(this);$("html, body").stop().animate({scrollTop:$(t.attr("href")).offset().top},1500,"easeInOutExpo");e.preventDefault()})});$("body").scrollspy({target:".navbar-fixed-top"});$(".navbar-collapse ul li a").click(function(){$(".navbar-toggle:visible").click()})
        </script>
        %s
    </body>
    </html>""" % (
        phone, address, email, map1, orgname, facebooklink, youtubelink,
        twitterlink, map2, backstretch1, backstretch2, calendarevents)

    html = (part1 + events + part2).encode("utf-8", 'replace')

    return html
