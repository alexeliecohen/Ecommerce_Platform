<template>
    <div>
       <!-- <current-loc></current-loc> -->
        <!--Above the product details page-->
        <div class="detail cle z-detail-box">
            <div class="detail_wrap">
                <div class="detail_img" id="detail_img">
                    <div class="pic_view">
                        <a class="MagicZoomPlus" id="Zoomer" style="position: relative; display: inline-block; text-decoration: none; outline: 0px; overflow: hidden; width: auto; height: auto;">
                            <img :src="curShow.image" alt="" style="opacity: 1;">
                            <div class="MagicZoomPup" style="z-index: 10; position: absolute; overflow: hidden;  visibility: hidden; width: 190px; height: 190px; opacity: 0.5;"></div>
                            <div class="MagicZoomPlusHint" style="display: block; overflow: hidden; position: absolute; visibility: visible; z-index: 1; left: 2px; right: auto; top: 2px; bottom: auto; opacity: 0.75; max-width: 376px;"></div>
                        </a>
                    </div>
                    <div class="item-thumbs" id="item-thumbs">
                        <!-- <a class="prev" href="javascript:void(0);" @click="ImagePrev"></a>
                        <a class="next" href="javascript:void(0);" @click="ImageNext"></a> -->
                        <div class="bd">
                            <div class="tempWrap" style="overflow:hidden; position:relative; width:330px">
                                <ul class="cle" style="display: flex;justify-content: center;width: 330px; position: relative; overflow: hidden; padding: 0px; margin: 0px; left: 0px;">
                                    <li v-for="(item,index) in proDetail.images" :class="{'current': index===curIndex}" @click="replaceShow(index,item)" :key="item.id">
                                        <a>
                                            <img :src="item.image" alt="">
                                        </a>
                                    </li>
                                </ul>
                            </div>
                        </div>

                    </div>
                </div>
                <div class="item-info" id="item-info">
                    <dl class="loaded">
                        <dt class="product_name">
                        <h1>{{proDetail.name}}</h1>
                        <p class="desc"> <span class="gray">{{proDetail.goods_brief}}</span> </p>
                        </dt>
                        <dd class="property">
                            <ul>
                                <li v-if="proDetail.ship_free">This item has free shipping and won't be included in the shippping cost of your order!</li>
                                <li>
                                    <span class="lbl">Market Price</span> 
                                        <em v-if="proDetail.shop_price != proDetail.market_price" class="cancel">${{proDetail.market_price}}</em>
                                        <em v-else >${{proDetail.market_price}}</em>
                                    </li>
                                <li v-if="proDetail.shop_price != proDetail.market_price">
                                    <span class="icon_promo">FLASH SALE</span> <span class="lbl">Sale Price</span>
                                    <span class="unit"> <strong class="nala_price red" id="ECS_SHOPPRICE">${{proDetail.shop_price}}</strong> </span>  
                                    <span class="timedown" id="timedown"></span>
                                </li>
                                <li>
                                    <span class="lbl">Quantity Sold</span><span>Recently Sold<em class="red">{{proDetail.sold_num}}</em> Units</span></li>
                            </ul>
                        </dd>
                        <dd class="tobuy-box cle">
                            <ul class="sku">
                                <li class="skunum_li cle">
                                    <span class="lbl">Quantity</span>
                                    <div class="skunum" id="skunum"> <span class="minus" title="Reduce 1 Quantity" @click="reduceNum"><i class="iconfont">-</i></span>
                                        <input id="number" name="number" type="text" min="1" v-model="buyNum"  onchange="countNum(0)">
                                        <span class="add" title="Increase 1 Quantity" @click="addNum"><i class="iconfont">+</i></span> <cite class="storage"> Units</cite>
                                    </div>
                                    <div class="skunum" id="skunum">

                                        <cite class="storage">(<font id="shows_number">{{proDetail.goods_num}} Units</font>)</cite>

                                    </div>
                                </li>
                                <li class="add_cart_li">
                                    <a class="btn" id="buy_btn" @click="addShoppingCart">
                                        <i class="iconfont">&#xe600;</i>
                                        Add to Cart</a>

                                    <a v-if="hasFav" id="fav-btn" class="wishlistbtn" @click="deleteCollect">
                                        <i class="iconfont">&#xe613;</i>Added!</a>
                                  <a v-else class="wishlistbtn" @click="addCollect">
                                    <i class="iconfont">&#xe613;</i>Add to Wishlist</a>
                                </li>
                            </ul>
                        </dd>
                    </dl>
                </div>
            </div>

        </div>

        <!--Below product details page-->
        <div class="detail_bgcolor">
            <div class="z-detail-box cle">
                <div class="z-detail-left">
                    <div class="taocan_bd">
                        <div class="product_tabs">
                            <div class="sectionbox z-box" id="spxqitem">
                                <div class="spxq_main">
                                    <div>
                                        <div>
                                            <table>
                                                <tbody>
                                                <tr>
                                                    <td width="20%" class="th"> Product Name :</td>
                                                    <td width="80%"> {{proDetail.name}}</td>
                                                </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                        <p>&nbsp; </p>
                                    </div>
                                    <div class="spxq_dec">
                                        <p v-html="proDetail.goods_desc">
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <hot-sales></hot-sales>
            </div>
        </div>
        <ReviewContainer class="mt-4" />
        <model ref="model"></model>
    </div>
</template>
<script>
import cookie from '../../static/js/cookie';
import currentLoc from './current-loc/current-loc';
import "bootstrap-vue/dist/bootstrap-vue.css";
import hotSales from './hotSales';
import model from './model'
import { mapGetters } from 'vuex';
import { getGoodsDetail, getFav, addFav, delFav, addShopCart,getShopCart, postReviews, getReviews} from '../../api/api';
import ReviewContainer from "./Review_Container";
  export default {
    data () {
        return {
            productId: '',
            curIndex: 0, 
            curShow: {
                desc: 'First detail',
                src: './images/1(1).jpg'
            },
            hasFav: false,
            proDetail: {
            },
            buyNum:1
        };
    },
    components: {
        'current-loc': currentLoc,
        'hot-sales': hotSales,
         model,
         ReviewContainer
    },
    props: {

    },
    created () {
        this.productId = this.$route.params.productId;
        var productId = this.productId
        if(cookie.getCookie('token')){
          getFav(productId).then((response)=> {
            this.hasFav = true
          }).catch(function (error) {
            console.log(error);
          });
        }
        this.getDetails();
    },
    watch: {

    },
    computed: {
    },
    methods: {
        getDetails () {
          getGoodsDetail(this.productId)
            .then((response)=> {
                console.log(response.data);
                this.proDetail = response.data;
                this.curShow = this.proDetail.images[0];
            }).catch(function (error) {
                console.log(error);
            });
        },
        reduceNum () {
            this.buyNum = this.buyNum === 1 ? 1 : this.buyNum - 1;
        },

        hasFaved () {

        },

        addNum () {
            this.buyNum = this.buyNum + 1;

        },
        addShoppingCart () { 
            addShopCart({
                goods: this.productId,
                nums: this.buyNum,
            }).then((response)=> {
                this.$refs.model.setShow();
                this.$store.dispatch('setShopList');

            }).catch(function (error) {
                console.log(error);
            });
        },
        addCollect () {
          addFav({
              goods: this.productId
          }).then((response)=> {
                console.log(response.data);
                this.hasFav = true
            }).catch(function (error) {
                console.log(error);
            });
        },

        deleteCollect () {
          delFav(this.productId).then((response)=> {
            console.log(response.data);
            this.hasFav = false
          }).catch(function (error) {
            console.log(error);
          });
        },
        ImagePrev () {
            this.curIndex = this.curIndex === 0 ? 0 : this.curIndex - 1;
        },
        ImageNext () {
            this.curIndex = this.curIndex === this.proDetail.images.length - 1 ? this.proDetail.images.length - 1 : this.curIndex + 1;
        },
        replaceShow (index, item) {
            this.curIndex = index;
            this.curShow = item;
        }
    }
}
</script>
<style >


.tabs_bar_warp {
    height:48px;
    width:970px
}

.tabs_bar_warp {
    height:48px;
    width:970px
}
.tabs_bar {
    height:48px;
    width:968px;
    background:#f3f3f3;
    border:1px solid #ccc;
    z-index:999;
    top:0
}
.tabs_bar ul {
    width:100%;
    height:48px
}
.tabs_bar ul li {
    _bottom:-1px;
    z-index:999;
    position:relative;
    display:block;
    float:left;
    height:48px;
    line-height:48px
}
.tabs_bar ul li a {
    border-bottom:1px solid #ccc;
    border-right:1px solid #ccc;
    padding:0 35px;
    display:block
}
.tabs_bar ul li a:hover {
    text-decoration:none;
    background:#fff
}
.tabs_bar ul li.current_select a {
    text-decoration:none;
    background:#fff;
    border-bottom:1px solid #fff
}
.tabs_bar ul li a em {
    color:#2462ff;
    font-weight:bold
}
.tabs_bar li.tab-buy {
    color:#2462ff;
    float:right;
    padding-right:94px;
    position:relative;
    text-align:right;
    width:200px;
    margin-right:0;
    visibility:hidden
}
.tabs_bar li.tab-buy strong {
    font:24px/48px arial;
    padding:0 4px
}
.tabs_bar li.tab-buy a.btn {
    position:absolute;
    right:8px;
    top:6px;
    font-size:16px;
    height:23px;
    line-height:22px;
    padding:5px 12px;
    background:#2462ff
}
.tabs_bar li.tab-buy a.btn:hover {
    background:#1441b1
}
.tabs_bar li.tab-buy a.wishlistbtn {
    position:absolute;
    right:8px;
    top:8px;
    height:30px;
    line-height:30px;
    cursor:default;
    background:#e5e5e5;
    padding:0 12px;
    border-color:#ddd;
    box-shadow:none
}
.tabs_bar li.tab-buy a.wishlistbtn:hover {
    background:#e5e5e5
}
/*.sectionbox h2.tit {*/
    /*background:url(images/spxq_nav_bg.png) 0 0 no-repeat;*/
    /*height:27px;*/
    /*padding:0 15px;*/
    /*margin-bottom:10px*/
/*}*/
/*.sectionbox h2.tit span {*/
    /*background:url(images/spxq_nav_bg_t.png) -9999px 0 no-repeat;*/
    /*display:block;*/
    /*height:0;*/
    /*padding-top:27px;*/
    /*overflow:hidden*/
/*}*/
/*.sectionbox h2.tit1 span {*/
    /*background-position:0 -52px*/
/*}*/
/*.sectionbox h2.tit2 span {*/
    /*background-position:0 -80px*/
/*}*/
/*.sectionbox h2.tit3 span {*/
    /*background-position:0 -108px*/
/*}*/
/*.sectionbox h2.tit4 span {*/
    /*background-position:0 -136px*/
/*}*/
/*.sectionbox h2.tit5 span {*/
    /*background-position:0 -164px*/
/*}*/
/*.sectionbox h2.tit6 span {*/
    /*background-position:0 -192px*/
/*}*/
/*.sectionbox h2.tit7 span {*/
    /*background-position:0 -220px*/
/*}*/
/*.sectionbox h2.tit8 span {*/
    /*background-position:0 -248px*/
/*}*/
/*.sectionbox h2.tit9 span {*/
    /*background-position:0 -276px*/
/*}*/
/*.sectionbox h2.tit10 span {*/
    /*background-position:0 -304px*/
/*}*/
/*.sectionbox h2.tit11 span {*/
    /*background-position:0 -332px*/
/*}*/
/*.sectionbox h2.tit12 span {*/
    /*background-position:0 4px*/
/*}*/
/*.sectionbox h2.tit13 span {*/
    /*background-position:0 -24px*/
/*}*/
/*.sectionbox h2.tit14 span {*/
    /*background-position:0 -360px*/
/*}*/
.sectionbox div img {
    vertical-align:top
}
.sectionbox div img.img_error {
    width:300px;
    height:200px;
    display:block
}
.sectionbox .ping_more a {
    display:block;
    margin-top:20px;
    height:31px;
    line-height:31px;
    text-align:center;
    font-weight:bold;
    background-color:#f4f4f4;
    border:1px solid #e4e4e4
}
.sectionbox .ping_more a span {
    color:#666;
    font-weight:normal
}
.sectionbox .ping_more a:hover {
    background-color:#eee;
    text-decoration:none
}
.z-box {
    padding:20px;
    border:1px solid #ccc;
    border-top:0
}


.spxq_main {
    font-size:14px;
    line-height:24px
}
/*.spxq_main .nala_say {*/
    /*line-height:28px;*/
    /*background:url(images/nalasay-bg.jpg) 0 0 no-repeat;*/
    /*padding:0 20px 0 140px;*/
    /*min-height:110px;*/
/*+height:110px*/
/*}*/
.spxq_main img {
    display:block;
    margin:0 auto
}
.spxq_main .spxq_top {
    margin:25px 0 0;
    font-size:16px;
    color:#2462ff;
    font-weight:bold
}
.spxq_main .spxq_dec div {
    margin-bottom:20px
}
.spxq_main table {
    width:100%
}
.spxq_main table td {
    border:1px solid #e5e5e5;
    padding:5px 10px
}
.spxq_main table td.th {
    background-color:#f5f5f5;
    font-weight:bold;
    width:70px;
    text-align:right
}
.spxq_main table td strong {
    font-weight:400
}
.spxq_main table td div,.spxq_main table td span {
    display:block;
    margin-bottom:4px
}
.spxq_main h3 {
    font-size:20px;
    margin:20px 0 10px;
    color:#2462ff;
    border-bottom:1px solid #2462ff;
    padding-bottom:5px
}
.spxq_main p {
    margin-bottom:10px
}
.spxq_dec table td {
    border:0;
    padding:0
}

.z-detail-point-box {
    border:1px solid #ccc
}
.z-detail-point-box-left {
    padding:20px;
    width:520px;
    overflow:hidden;
    float:left;
    border-right:1px solid #ccc;
}

.z-detail-point-box-right {
    width:365px;
    float:right;
    font-size:14px;
    padding-top:16px;
    background:#fcfcfc;
    height:96px;
}
.z-detail-point-box-right div {
    font-size:12px;
    padding:5px 20px;
    line-height:20px;
    color:#999999;
}
.z-detail-point-box-right div font {
    color:#2462ff;
}
.z-detail-point-box-right div a.go_btn {
    position:absolute;
    right:10px;
    top:3px
}
.z-detail-point-box-right div.good_com_box {
    position:relative;
    z-index:99
}
.z-detail-point-box-right div a.good_com {
    color:#2462ff;
    margin-right:5px
}
.z-detail-point-box-right div.good_com_box .good_com_tips {
    position:absolute;
    width:200px;
    padding:15px;
    border:1px solid #ffb97c;
    line-height:20px;
    color:#666;
    background:#fff7f0;
    left:22px;
    _left:1px;
    top:30px;
    display:none
}
.z-com-box-head {
    height:50px;
    border-bottom:1px solid #ccc;
    background:#f3f3f3;
    padding:0 20px;
    line-height:50px;
    font-size:14px
}




.detail_bgcolor {
    padding-top:16px;
    padding-bottom:40px;
    height: 200px;
}
.z-detail-box {
    width:1196px;
    margin:0 auto
}

.z-detail-left {
    width:970px;
    float:left;
    background-color:#fff
}


.detail {
    border:1px solid #d9dbe8;
    /*border-top-color:#666;*/
    /*background:#fff url(./images/seemore-bg.png) right 0 repeat-y;*/
    /*background:#fff url(./images/seemore-bg.png) right 0 repeat-y;*/
}
.detail_wrap {
    width: 1000px;
    margin: 0 auto;
}
.detail_img {
    width:410px;
    position:relative;
    float:left
}
.detail_brand {
    display:none
}
.detail_img .pic_view {
    width:380px;
    height:380px;
    margin:20px auto 0;
    position:relative
}

.detail_img {
    width:410px;
    position:relative;
    float:left
}
.detail_brand {
    display:none
}
.detail_img .pic_view {
    width:380px;
    height:380px;
    margin:20px auto 0;
    position:relative
}
.detail_img .pic_view img {
    width:380px;
    height:380px;
    object-fit: scale-down;
}
#pic-view {
    position:absolute;
    top:0;
    left:0;
    z-index:2
}
.item-thumbs {
    padding:15px 0;
    height:58px;
    overflow:hidden;
    position:relative
}
.item-thumbs ul {
    text-align:center;
    height:58px;
    width:330px;
    overflow:hidden;
    padding-left:8px;
    margin:0 auto
}
.item-thumbs li {
    width:56px;
    height:56px;
    overflow:hidden;
    border:1px solid #ddd;
    margin:0;
    margin-right:8px;
    zoom:1;
    cursor:pointer;
    float:left;
    display:block
}
.item-thumbs li.current {
    border-color:#2462ff
}
.item-thumbs .bd {
    width:330px;
    padding-left:10px;
    overflow:hidden;
    position:relative;
    margin:0 auto
}
.item-thumbs li a {
    display:block
}
.item-thumbs li img {
    width:56px;
    height:56px;
    object-fit: cover;
}
#item-thumbs .prev {
    display:block;
    position:absolute;
    width:15px;
    height:30px;
    background:url(./images/footprint-arr.png) no-repeat;
    top:30px;
    left:18px
}
.item-thumbs .next {
    display:block;
    position:absolute;
    width:15px;
    height:30px;
    background:url(./images/footprint-arr.png) -15px 0 no-repeat;
    top:30px;
    right:18px
}
.item-thumbs div.arrow {
    position:absolute;

    top:0;
    color:#2462ff
}
.item-thumbs a.left_btn,.item-thumbs a.right_btn {
    position:absolute;
    color:#999;
    display:block;
    height:58px;
    line-height:58px;
    font-size:16px;
    top:15px
}
.item-thumbs a.left_btn:hover,.item-thumbs a.right_btn:hover {
    text-decoration:none;
    color:#ccc
}
.item-thumbs a.left_btn {
    left:20px
}
.item-thumbs a.right_btn {
    right:20px
}



.item-info {
    float:left;
    width:570px;
    color:#999;
    position:relative
}
.item-info dl {
    height:425px;
    padding-bottom:10px;
    background:url(./images/loading_nala.gif?0428) 250px 200px no-repeat
}
.item-info dl.loaded {
    height:auto;
    background:0
}
.item-info .product_name {
    color:#333;
    margin:0 15px;
    padding:18px 6px 0;
    border-bottom:1px solid #f4f4f4
}
.item-info .product_name h1 {
    font-size:18px
}
.item-info .product_name h1 span.free {
    background-color:#48b7ae;
    color:#fff;
    margin-left:8px;
    text-align:center;
    border-radius:2px;
    display:inline-block;
    height:22px;
    line-height:21px;
    color:#fff;
    font-size:14px;
    font-weight:normal;
    width:66px
}
.item-info .product_name .desc {
    line-height:18px;
    padding:6px 0 12px;
    display:block
}
.item-info .product_name .desc span.red {
    margin-right:13px
}
.item-info dd {
    padding:10px 16px 0 20px
}
.item-info dd .lbl {
    display:inline-block;
    width:52px;
    color:#666
}
.item-info dd li {
    padding:5px 0;
    position:relative;
    width:100%
}
.item-info dd li .icon_promo,.item-info dd li span.t_ico {
    background-color:#2462ff;
    color:#fff;
    display:inline-block;
    height:20px;
    line-height:20px;
    margin-right:10px;
    padding:0 5px;
    border-radius:2px;
    overflow:hidden;
    vertical-align:middle
}
.item-info dd li span.t_ico {
    width:66px;
    text-align:center;
    font-size:14px;
    padding:0 0 1px
}
.item-info dd li .icon_promo {
    position:relative;
    top:-4px
}
.item-info dd li span.xszk {
    background:#fa6569;
    position:relative;
    top:-4px;
    font-size:12px
}
.item-info dd li span.mj {
    background:#95ce67
}
.item-info dd li span.mz {
    background:#fdb64a;
    top:-2px
}
.item-info dd li span.link {
    display:inline-block;
    vertical-align:middle;
    padding-left:5px
}
.item-info dd li span.link a {
    color:#39f;
    text-decoration:underline
}
.item-info dd li span.link a:hover {
    color:#72b7fb
}
.item-info dd li em.cancel {
    text-decoration:line-through
}
.item-info dd li em.red {
    margin:0 4px
}
.item-info dd li em.red a {
    color:#2462ff
}
.item-info .property .unit {
    display:inline-block
}
.item-info .property .unit em {
    color:#666;
    margin-right:4px
}
.item-info .property .unit em.rmb {
    font-size:14px
}
.item-info .property .unit em.red {
    color:#2462ff;
    margin:0
}
.item-info .property .nala_price {
    font-size:24px;
    font-family:Arial;
    font-weight:bold;
    padding:0 10px 0 0;
    line-height:28px
}
.item-info dd.tobuy-box .lbl {
    float:left;
    width:50px;
    margin-top:6px
}


.skunum_li {
    margin-bottom:15px
}
.skunum {
    float:left;
    height:32px;
    font-size:0;
    overflow:hidden;
    padding-left:5px
}
.skunum span {
    float:left;
    display:block;
    width:28px;
    height:30px;
    border:1px solid #ccc;
    background-color:#eee;
    text-align:center;
    font-size:20px;
    overflow:hidden;
    line-height:28px;
    color:#777;
    cursor:pointer
}
.skunum span.add {
    margin-left:-2px
}
.skunum span:active {
    background-color:#ccc
}
.skunum input {
    float:left;
    display:block;
    width:66px;
    height:14px;
    padding:8px 0;
    line-height:14px;
    border:0;
    border-top:1px solid #ccc;
    border-bottom:1px solid #ccc;
    text-align:center;
    font-size:14px;
    background-color:#fff
}
.skunum cite {
    margin-left:5px;
    color:#999;
    font-size:12px;
    padding-top:10px;
    float:left
}
.skunum cite em {
    margin:0 4px
}


.tobuy-box .add_cart_li p {
    margin-bottom:5px
}
.tobuy-box .add_cart_li .btn,.tobuy-box .add_cart_li .wishlistbtn {
    font-size:16px;
    padding:10px 20px 12px
}
.tobuy-box .add_cart_li .wishlistbtn {
    margin-left:12px;
    font-size:14px
}
.tobuy-box .add_cart_li i.iconfont {
    vertical-align:1px;
    margin-right:4px
}
.tobuy-box .add_cart_li .off {
    background-color:#e9e9e9;
    font-size:16px;
    color:#bbb;
    display:inline-block;
    padding:7px 20px 9px;
    vertical-align:middle
}
.btn,.btn-css3 {
    display:inline-block;
    padding:5px 12px;
    height:16px;
    line-height:16px;
    _line-height:18px;
    border:1px solid #1844b4;
    border-radius:3px;
    font-size:100%;
    color:#fff;
    background-color:#2462ff;
    overflow:hidden;
    vertical-align:middle
}
.btn:hover,.btn-css3:hover {
    text-decoration:none;
    color:#fff;
    background:#4d7fff;
}
.btn img,.btn-css3 img {
    vertical-align:middle
}
.wishlistbtn {
    display:inline-block;
    padding:5px 12px;
    height:16px;
    line-height:16px;
    border:1px solid #c4c4c4;
    border-radius:2px;
    font-size:100%;
    color:#ffffff;
    background-color:#e67d22;
    background-repeat:repeat-x;
    vertical-align:middle
}
.wishlistbtn:hover {
    text-decoration:none;
    color:#ffffff;
    background:#f19e56;
}


</style>
