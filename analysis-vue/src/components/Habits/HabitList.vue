<template>
    <div id="habitListApp">
        <div class="container">
            <div class="habitList">
                <h1 class="text-center mt-3">Hedefler</h1>
                <div class="row w-100 m-0">
                    <div class="col-md-4 col-xs-12" v-for="habit in getHabitList" :key="habit.id">
                        <a @click='goToHabit(habit.slug)'>
                            <div class="card mt-4">
                                <div class="card-header">
                                    <p class="habit-title">{{habit.title}}</p>
                                    <p class="habit-description">{{habit.description}}</p>
                                </div>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
            <div class="row w-100 mt-5 d-flex justify-content-center">
                <button type="button" class="create-habit-button" data-toggle="modal" data-target="#exampleModalCenter">
                Rutin Oluştur
                </button>

                <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered" id="modalDialog" role="document">
                        <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLongTitle">Rutin Oluştur</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            <form method="POST">
                                <div class="field title">
                                    <input v-model="title" class="form-control" placeholder="İsim" required type="text">
                                </div>      
                                <div class="field description">
                                    <input v-model="description" class="form-control" placeholder="Açıklama" type="text">
                                </div>
                                <div class="field category">
                                    <select v-model="category" class="form-control">
                                        <option v-for="category in getCategoryList" :key="category.slug" :value="category">{{category.title}}</option>
                                    </select>
                                </div>
                                <div class="field daily_goal">
                                    <input v-model="daily_goal" class="form-control" :placeholder="`Günlük '${category.daily_goal_type}' Hedefi`" type="text">
                                </div>
                                <div class="field end_date">
                                    <input v-model="end_date" class="form-control" placeholder="Bitirilecek Tarih" required type="date">
                                </div>  
                            </form>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="close-button text-white" data-dismiss="modal">Kapat</button>
                            <button @click="createHabit" type="button" class="button button-ocean-blue form-button">Oluştur</button>
                        </div>
                        </div>
                    </div>
                </div> 
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['activeComponent'],
    data(){
        return{
            habitList: [],
            categoryList: [],
            title: '',
            description: '',
            category: '',
            daily_goal: 0,
            end_date: '',
        }
    },
    computed: {
        getCategoryList(){
            if (this.categoryList.length < 1){
                this.categoryList = this.$store.getters.getCategoryList;
            }
            return this.categoryList;
        },
        getHabitList(){
          if (this.habitList.length < 1)  {
              this.habitList = this.$store.getters.getHabitList;
          }
          return this.habitList;
        }
    },    
    methods: {
        createHabit(){
            let habit = {
                title: this.title,
                description: this.description,
                category: this.category.id,
                daily_goal: this.daily_goal,
                end_date: this.end_date,
            }
            this.$store.dispatch('createHabitAsync', habit);
        },
        goToHabit(habitSlug){
            this.$store.state.habitSlug = habitSlug;
            this.$emit('activeComponent', 'SingleHabit');
        }
    },        
}
</script>

<style scoped>
.col-md-4 a{
    text-decoration: none;
    cursor: pointer;
}

.card:hover{
    box-shadow: 0px 0px 5px 5px rgb(59, 208, 185);
}

.card-header{
    min-height: 100px;
}

.habit-title{
    color: black;
    font-size: 1.5em;
}

.habit-description{
    color: darkgray;
    font-size: 0.9em;
}

.create-habit-button{
    border: 1px solid rgb(59, 208, 185);
    background-color: rgb(59, 208, 185);
    color: white;
    letter-spacing: 1.2px;
    width: 150px;
    height: 60px;
    font-size: 1.1em;
}


.form-title{
    margin-top: 20px;
}

.field input{
    height: 50px;
    border-radius: 0px;
    margin-bottom: 20px;
    margin-top: 10px;
    outline: 0px;
}

.form-button{
    width: 100px;
    height: 40px;
}

.close-button{
    background-color: black;
    width: 100px;
    height: 40px;
}

</style>