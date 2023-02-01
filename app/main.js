


Vue.component('chat-message',{
    props:['message','type'],

    template:`
    <div v-bind:class="[type?'left':'right']">
    <div class="image">
        <img src="" v-if="type==false">
        <img src="./BOT.svg" alt="" v-else>
    </div>
        <div class="text">
            {{message}}
        </div>
    </div>
    `
})
var app = new Vue({
    el:"#app",
    data:{
        name:"mark",
        showFab:false,
        showChat:false,
        messages:[],
        text:''
    },
    methods:{
        showEnter(e){
               var em = this;
                if(e.target.className == "fab" || e.target.parentElement.className == "fab"){
                    this.showFab = true;
                }

        },
        hideLeave(e){
            this.showFab = false;
        },
        openChat(){
            this.showChat = true;
        },
        closeChat(){
            this.showChat = false;
        },
        sendMsg(){
            var text = this.text;
            var vm = this;
            if(this.text != ""){
                this.messages.push({id:Math.random()*10000,type:false,message:this.text}),
                this.text = '';
                var url = `http://localhost/api/bot?query="${text}"`
                axios.get(url).then(e=>{
                    vm.messages.push({id:Math.random()*10000,type:true,message:e.data.bot_response})
                })
            }
            // fetch('/api/bot?query='+vm.text).then(function(e){
            //     console.log(e)
            // }).catch(function(err){
            //     console.log(err)
            // })
        }
    }
})


