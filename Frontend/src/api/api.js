import axios from 'axios';


let host = 'http://shop.projectsedu.com';
// let host = 'http://127.0.0.1:8000';
let host354 = 'http://173.249.5.177:443';

//获取商品类别信息
export const queryCategorygoods = params => { return axios.get(`${host354}/indexgoods/`) }

//获取首页中的新品
export const newGoods = params => { return axios.get(`${host}/newgoods/`) }

//获取轮播图
export const bannerGoods = params => { return axios.get(`${host}/banners/`) }

//获取商品类别信息
export const getCategory = params => {
  if('id' in params){
    return axios.get(`${host354}/categorys/`+params.id+'/');
  }
  else {
    return axios.get(`${host354}/categorys/`, params);
  }
};


//获取热门搜索关键词
export const getHotSearch = params => { return axios.get(`${host}/hotsearchs/`) }

//获取商品列表
export const getGoods = params => { return axios.get(`${host354}/goods/`, { params: params }) }

//商品详情
export const getGoodsDetail = goodId => { return axios.get(`${host354}/goods/${goodId}`+'/') }

//获取购物车商品
export const getShopCarts = params => { return axios.get(`${host354}/shopcarts/`) }
// 添加商品到购物车
export const addShopCart = params => { return axios.post(`${host354}/shopcarts/`, params) }
//更新购物车商品信息
export const updateShopCart = (goodsId, params) => { return axios.patch(`${host354}/shopcarts/`+goodsId+'/', params) }
//删除某个商品的购物记录
export const deleteShopCart = goodsId => { return axios.delete(`${host354}/shopcarts/`+goodsId+'/') }

//收藏
export const addFav = params => { return axios.post(`${host354}/userfavs/`, params) }

//取消收藏
export const delFav = goodsId => { return axios.delete(`${host354}/userfavs/`+goodsId+'/') }

export const getAllFavs = () => { return axios.get(`${host354}/userfavs/`) }

//判断是否收藏
export const getFav = goodsId => { return axios.get(`${host354}/userfavs/`+goodsId+'/') }

//登录
export const login = params => {
  return axios.post(`${host}/login/`, params)
}

//注册

export const register = parmas => { return axios.post(`${host354}/users/`, parmas) }

//短信
export const getMessage = parmas => { return axios.post(`${host}/code/`, parmas) }


//获取用户信息
export const getUserDetail = () => { return axios.get(`${host354}/users/1/`) }

//修改用户信息
export const updateUserInfo = params => { return axios.patch(`${host354}/users/1/`, params) }


//获取订单
export const getOrders = () => { return axios.get(`${host354}/orders/`) }
//删除订单
export const delOrder = orderId => { return axios.delete(`${host354}/orders/`+orderId+'/') }
//添加订单
export const createOrder = params => {return axios.post(`${host354}/orders/`, params)}
//获取订单详情
export const getOrderDetail = orderId => {return axios.get(`${host354}/orders/`+orderId+'/')}


//获取留言
export const getMessages = () => {return axios.get(`${host354}/messages/`)}

//添加留言
export const addMessage = params => {return axios.post(`${host354}/messages/`, params, {headers:{ 'Content-Type': 'multipart/form-data' }})}

//删除留言
export const delMessages = messageId => {return axios.delete(`${host354}/messages/`+messageId+'/')}

//添加收货地址
export const addAddress = params => {return axios.post(`${host354}/address/`, params)}

//删除收货地址
export const delAddress = addressId => {return axios.delete(`${host354}/address/`+addressId+'/')}

//修改收货地址
export const updateAddress = (addressId, params) => {return axios.patch(`${host354}/address/`+addressId+'/', params)}

//获取收货地址
export const getAddress = () => {return axios.get(`${host354}/address/`)}
