<template>
    <!-- I think "message" are comments/reviews but I'm not sure -->
  <div class="my_nala_centre ilizi_centre">
    <div class="ilizi cle">
        <div class="box">
            <div class="box_1">
                <div class="userCenterBox boxCenterList clearfix" style="_height:1%; font-size:14px;">
                    <h5><span>My Message</span></h5>
                    <div class="blank"></div>
                    <div class="blank"></div>
                    <div class="message-all">
                        <ul>
                            <li v-for="(item,index) in messageAll" :key="index">
                                <div>
                                    <span v-if="item.message_type===1">Leave a Message</span>
                                    <span v-if="item.message_type===2">Complaint: </span>
                                    <span v-if="item.message_type===3">Ask: </span>
                                    <span v-if="item.message_type===4">After Sales: </span>
                                    <span v-if="item.message_type===5">Buying: </span>
                                    <span>{{item.subject}}</span>
                                    <span>（{{item.add_time}}）</span>
                                </div>
                                <div>
                                  {{item.message}}
                                </div>
                                <div>
                                    <a @click="deleteMessage(index, item.id)">Delete</a>
                                    <a :href="(item.file)">View Uploaded Files</a>

                                </div>

                            </li>
                        </ul>
                    </div>
                    <form action="" method="post" enctype="multipart/form-data" name="formMsg">
                        <table width="100%" border="0" cellpadding="3">
                            <tbody><tr>
                                <td align="right">Message Type: </td>
                                <td>
                                    <input type="radio" id="one" value="1" v-model="message_type">
                                    <label for="one">Leave a Message</label>
                                    <input type="radio" id="two" value="2" v-model="message_type">
                                    <label for="two">Complaint</label>
                                    <input type="radio" id="three" value="3" v-model="message_type">
                                    <label for="three">Ask</label>
                                    <input type="radio" id="four" value="4" v-model="message_type">
                                    <label for="four">After Sale</label>
                                    <input type="radio" id="five" value="5" v-model="message_type">
                                    <label for="five">Buying</label>

                                    <!-- <input name="msg_type" type="radio" value="0" checked="checked">
                                                            <input type="radio" name="msg_type" value="1">
                                                            <input type="radio" name="msg_type" value="2">
                                                            <input type="radio" name="msg_type" value="3">
                                                            <input type="radio" name="msg_type" value="4">
                                    -->
                                </td>
                            </tr>
                            <tr>
                                <td align="right">Subject: </td>
                                <td><input name="msg_title" type="text" size="30" class="inputBg" v-model="subject"></td>
                            </tr>
                            <tr>
                                <td align="right" valign="top">Message: </td>
                                <td><textarea name="msg_content" cols="50" rows="4" wrap="virtual" class="B_blue" v-model="message"></textarea></td>
                            </tr>
                            <tr>
                                <td align="right">Upload Files</td>
                                <td><input type="file" name="message_img" size="45" class="inputBg" @change="preview"></td>
                            </tr>
                            <tr>
                                <td>&nbsp;</td>
                                <td><input type="hidden" name="act" value="act_add_message">
                                    <!-- <input type="submit" value="提 交" class="bnt_bonus"> -->
                                    <a class="btn_blue_1" @click="submitMessage">Submit</a>
                                </td>
                            </tr>
                            <tr>
                                <td>&nbsp;</td>
                                <td>
                                    <font color="red">Info: </font><br>
                                    You can upload files in the following formats: <br>gif、jpg、png、word、excel、txt、zip、ppt、pdf                      </td>
                            </tr>
                            </tbody></table>
                    </form>


                </div>
            </div>
        </div>
    </div>

  </div>
</template>
<script>
  import {getMessages, addMessage, delMessages} from '../../api/api'
    export default {
        data () {
            return {
                message_type: '', 
                subject: '',
                message: '',
                file: '',
                // DOES NOT SUPPORT FILE UPLOAD CURRENTLY
                messageAll: [
                    // {
                    //     id: 1234,
                    //     message_type: 1,
                    //     theme: '',
                    //     message: '',
                    //     time: '2017-07-19 21:20:25',
                    // },
                    // {
                    //     id: 5678,
                    //     message_type: 2,
                    //     theme: '',
                    //     message: '',
                    //     time: '2017-07-19 21:20:25',
                    // }
                ]
            };
        },
        props: {

        },
        components: {

        },
        created () {
            this.getMessage();
        },
        watch: {

        },
        computed: {

        },
        methods: {
            preview (e) {
                this.file = e.target.files[0]; //file info
                console.log(this.file);

            },
            submitMessage () {
                const formData = new FormData();
                formData.append('file',this.file);
                formData.append('subject',this.subject);
                formData.append('message',this.message);
                formData.append('message_type',this.message_type);
                addMessage(formData).then((response)=> {
                    this.getMessage();

                }).catch(function (error) {
                    console.log(error);
                });
            },
            getMessage () { 
              getMessages().then((response)=> {
                    console.log(response.data);
                    this.messageAll = response.data;
                }).catch(function (error) {
                    console.log(error);
                });
            },
            deleteMessage (index, id) {
                delMessages(id).then((response)=> {
                  alert("Successfully Deleted Message")
                  this.messageAll.splice(index,1);
                }).catch(function (error) {
                    console.log(error);
                });
            },
        }
    }
</script>
<style scoped>
.message-all {
    border-bottom: 1px solid #ccc;
}
.message-all  li{
    border-bottom: 1px solid #ddd;
    padding: 10px;
}

.my_nala_centre {
    float:right;
    width:970px;
    background-color:#fff
}
.ilizi_centre {
    background:0
}
.my_nala_centre .trade_mod .h301 a.more {
    font-size:14px;
    color:#666;
    font-weight:normal
}
.my_nala_centre .trade_mod .h301 a.more:hover {
    color:#2462ff
}

.my_nala_centre .something_interesting {
    margin-top:10px
}
.my_nala_centre .something_interesting ul {
    margin-left:20px
}
.my_nala_centre .something_interesting li {
    width:130px;
    text-align:center;
    float:left
}
.my_nala_centre .something_interesting b {
    font-weight:normal
}
.my_nala_centre .something_interesting em {
    font-size:12px;
    font-weight:bold;
    color:#2462ff
}
.my_nala_centre .relate_goods {
    border:1px solid #e4e4e4;
    border-top:0
}
.my_nala_centre .pagenav {
    padding:15px 10px;
    border-top:1px solid #e4e4e4
}
.ilizi_centre {
    background:0
}
.ilizi {
    border:1px solid #e4e4e4;
    padding:16px 18px;
    margin-bottom:10px;
    background:#fff
}
.ilizi .face,.iface .face {
    display:block;
    float:left;
    width:100px;
    height:100px;
    position:relative
}
.ilizi .edit_face,.iface .edit_face {
    position:absolute;
    height:20px;
    line-height:20px;
    width:100px;
    display:block;
    background:rgba(0,0,0,0.5);
    text-align:center;
    color:#fff;
    left:1px;
    bottom:-1px;
    _bottom:0;
    filter:progid:DXImageTransform.Microsoft.gradient(enabled='true',startColorstr='#77000000',endColorstr='#77000000');
    visibility:hidden;
    margin:0
}
.ilizi .face img,.iface .face img {
    width:100px;
    height:100px;
    border:1px solid #e4e4e4
}
.ilizi .ilizi_info {
    width:800px;
    float:right;
    height:100px
}

.btn_blue_1{
  display: inline-block;
  padding: 4px 12px;
  height: 24px;
  line-height: 25px;
  _line-height: 18px;
  border: 1px solid #1844b4;
  border-radius: 3px;
  font-size: 100%;
  color: #fff;
  background-color: #2462ff;
  overflow: hidden;
  vertical-align: middle;
  cursor: pointer;
  text-decoration: none;
  vertical-align: middle;
}


</style>
