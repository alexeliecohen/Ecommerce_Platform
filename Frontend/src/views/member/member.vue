<template>
    <div id="wrapper" class="cle">
        <div class="here cle">
            <a href="" @click="toIndex">Home</a>
            <code>></code>
            User Centre
        </div>
        <div class="my_nala_main">
            <member-menu></member-menu>
            <router-view></router-view>
        </div>
    </div>
</template>
<script>
import memberMenu from './member-menu';
    export default {
        data () {
            return {
                
            };
        },
        props: {
            
        },
        components: {
            'member-menu': memberMenu,
            // 'receive': receive
        },
        created () {
            
        },
        watch: {
            
        },
        computed: {

        },
        methods: {
            toIndex () { //Back to the homepage
                this.$router.push({name: 'index'});
            }
        }
    }
</script>
<style scoped>


.my_nala_main h3.my_nala {
    height:60px;
    border:1px solid #e7e7e7;
    border-bottom:0
}
.my_nala_main h3.my_nala a {
    display:block;
    height:60px;
    font-size:22px;
    text-align:center;
    line-height:60px;
    overflow:hidden
}
.my_nala_main h3.my_nala a:hover {
    text-decoration:none
}

</style>
