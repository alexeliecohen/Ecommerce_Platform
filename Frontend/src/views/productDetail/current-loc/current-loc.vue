<template>
    <div class="current-loc">
        <div class="breadcrumbs cle z-detail-box">
          <div class="menus">
            <a href="http://sx.web51.youxueshop.com/">Home</a>
            <code>&gt;</code>
            <a href="http://sx.web51.youxueshop.com/category.php?id=2">Fresh food</a>
            <code>&gt;</code>
            <a href="http://sx.web51.youxueshop.com/category.php?id=19">Rhizomes</a>
            <code>&gt;</code>
            Fresh fruit sweet and crisp single fruit about 800 grams
          </div>
      </div>
    
    </div>
  
</template>
<script>
  
  export default {
    data () {
        return {
            
        };
    },
    components: {
        
    },
    props: {
        
    },
    created () {
        
    },
    watch: {
        
    },
    computed: {

    },
    methods: {
        
    }
}
</script>
<style  lang='scss'>
.cle:after{
    visibility:hidden;
    display:block;
    font-size:0;
    content:'\20';
    clear:both;
    height:0
}
.cle{
    *zoom:1
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

canvas {
    -ms-touch-action:double-tap-zoom
}

.breadcrumbs {
    padding:0 5px 0 0;
    line-height:38px;
    color:#666
}
.breadcrumbs .menus {
    float:left
}
.breadcrumbs .menus a {
    margin-right:6px
}
.breadcrumbs .right {
    float:right;
    color:#bbb
}
.breadcrumbs .right i {
    font-size:20px;
    margin-right:5px;
    vertical-align:-2px
}
.breadcrumbs .right .code {
    color:#fafafa;
    margin-right:30px;
    display:inline-block
}

</style>
