export class User{
    constructor(username,email,password){
        this.username = username;
        this.email = email;
        this.password = password;
        this.id = Date.now();
    }
}