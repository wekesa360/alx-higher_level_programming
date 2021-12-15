#!/usr/bin/node
module.exports = class Rectangle{
    constructor(w, h){
        if ( w > 0 && h > 0){
            this.width = w;
            this.height = h;
        }
    }
    print(){
        console.log('x'.repeat(this.width));
    }
    rotate (){
        let tmp = this.height;
        this.height = this.width;
        this.width = tmp;
    }
    double (){
        this.height *= 2;
        this.width *= 2;
    }
};