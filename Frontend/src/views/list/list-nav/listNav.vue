<template>
    <div class="sidebar">
        <div class="cate-menu" id="cate-menu">
            <div v-if="isObject" class="cat_info-container">
                <p class="cat_title" v-if="cateMenu && curCatIndex && cateMenu[curCatIndex]">{{cateMenu[curCatIndex].name}}</p>
                <p class="cat_title" v-else>{{currentCategoryName }}</p>
                <p id="total_count">Total Count: {{proNum}} Units</p>
            </div>
            <dl>
                <template v-for="(item, index) in cateMenu">
                    <dt :key="item.id"><a @click="changeMenu(item.id, index)">{{ item.name}}</a></dt>
                    <dd v-for="subItem in item.sub_cat"> <!-- Just ignore for now, it's being a pain -->
                        <a @click="changeMenu(subItem.id, index)">{{ subItem.name}}</a>
                    </dd>
                </template>
            </dl>
        </div>
    </div>
</template>
<script>
  export default {
    data () {
        return {
            cateType: '', //category
            curCatIndex: Number,
        };
    },
    components: {

    },
    props: {
        cateMenu: {
            default: function() {
                return {};
            }
        },
        proNum: { //number of products
            type: Number,
            default: 0
        },
        isArray:{
            default: function () {
              return false
            }
        },
        isObject: false,
        currentCategoryName: ""
    },
    created () {
    },
    watch: {
        currentCategoryName: {
            handler: function(val, oldval) {
                if (oldval != val)
                    this.curCatIndex = null
            }
        }
    },
    computed: {
    },
    methods: {
        changeMenu(id, index) {
            this.curCatIndex = index;
            this.$emit('on-change', id);
        }
    }
}
</script>
<style >
html {
    background:#fafafa;
    color:#333;
    _background-attachment:fixed
}
html.isPhone {
    min-width:1196px
}
body,h1,h2,h3,h4,h5,h6,hr,p,blockquote,dl,dt,dd,ul,ol,li,pre,form,fieldset,legend,button,input,select,textarea,th,td {
    margin:0;
    padding:0
}
body,button,input,select,textarea {
    font:12px/1.5 "Microsoft YaHei",Tahoma,Helvetica,Arial,simsun
}
address,cite,dfn,em,var,i {
    font-style:normal
}
ul,ol {
    list-style:none
}
fieldset,img {
    border:0
}
h1 {
    font-size:18px
}
h2 {
    font-size:14px;
    font-weight:bold
}
h3 {
    font-size:14px;
    font-weight:400
}
h4,h5 {
    font-size:12px;
    font-weight:400
}
input,textarea,button,select {
    font-size:12px;
    outline:0;
    resize:none;
    color:#333
}
button {
    cursor:pointer
}
table {
    border-collapse:collapse;
    border-spacing:0
}
.clear {
    clear:both;
    height:0;
    font-size:0;
    line-height:0;
    overflow:hidden
}
.cle:after,.clearfix:after,.clear_f:after,.cle_float:after {
    visibility:hidden;
    display:block;
    font-size:0;
    content:'\20';
    clear:both;
    height:0
}
.cle,.clearfix,.clear_f,.cle_float {
    *zoom:1
}

.cat_info-container {
    padding: 10px
}

.cat_title {
    font-weight: bold;
    font-size: 15px;
    margin-bottom: 10px;
}

.fl {
    float:left
}
.fr {
    float:right
}
a {
    text-decoration:none;
    color:#333;
    -webkit-transition:color .2s;
    -moz-transition:color .2s;
    -o-transition:color .2s;
    -ms-transition:color .2s;
    transition:color .2s
}
a:hover {
    color:#2462ff
}
a:focus,area:focus {
    outline:0
}
::selection {
    background:#2462ff;
    color:#fff
}
canvas {
    -ms-touch-action:double-tap-zoom
}
@font-face {
    font-family:'lizi';
    src:url('http://at.alicdn.com/t/font_1412819191_5742776.eot');
    src:url('http://at.alicdn.com/t/font_1412819191_5742776.eot?#iefix') format('embedded-opentype'),url('http://at.alicdn.com/t/font_1412819191_5742776.woff') format('woff'),url('http://at.alicdn.com/t/font_1412819191_5742776.ttf') format('truetype'),url('http://at.alicdn.com/t/font_1412819191_5742776.svg#iconfont') format('svg')
}
.here{padding:5px 0;color:#bbb}
.here i.iconfont{font-size:14px}
.here h1{display:inline;font-size:12px;color:#333;font-weight:normal}
.sidebar{width:214px;float:left}
.cate-menu{margin-bottom:12px;background-color:#fff}
.cate-menu h3{border:1px solid #ddd}
.cate-menu h3 a{display:block;height:26px;padding:14px 0 12px 12px;background-color:#fff;position:relative}
.cate-menu h3 a:hover{background-color:#fafafa;text-decoration:none}
.cate-menu h3 strong{font-size:18px;color:#333;letter-spacing:3px;font-weight:400}
.cate-menu h3 i{position:absolute;right:10px;top:23px;color:#999;font-size:12px}
.cate-menu dl{border:1px solid #eee;padding:10px 0}
.cate-menu dt{font-size:14px;padding:5px 0 5px 12px;color:#888}
.cate-menu dd a{display:block;padding:7px 0 7px 27px;background-color:#fff}
.cate-menu dd a:hover{background-color:#fafafa;text-decoration:none}
.cate-menu dd a i{color:#bbb;margin-left:5px}
.cate-menu dd.current a,.cate-menu dd.current a:hover{color:#2462ff;background-color:#f1f1f1}

</style>
