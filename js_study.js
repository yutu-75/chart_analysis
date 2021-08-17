let  table1Data =  [{
    id: 0,

    name: '王小虎0',

}, {
    id: 1,
    name: '王小虎1',

}, {
    id: 2,
    name: '王小虎2',

}, {
    id: 3,
    name: '王小虎3',

}, {
    id: 4,
    name: '王小虎4',

}, {
    id: 5,
    name: '王小虎5',

}, {
    id: 6,
    name: '王小量',

}]
let a = '说的、多少、都是、打算多少'
let v = a.split('、')
let data_list = []
for(let i=0;i < table1Data.length;i++){
        data_list.push(table1Data[i]['id'])
}
max_sum = data_list.sort().reverse()[0]
console.log(data_list.sort().reverse()[0])
for(let i=0;i < v.length;i++){
        table1Data.push({id:max_sum+i+1,name:v[i]})
}
// table1Data.push(v)
// console.log(v)
console.log(table1Data)

console.log( Boolean(''))




