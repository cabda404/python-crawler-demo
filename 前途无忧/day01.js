const CryptoJS = require('crypto-js');


// e = "/api/job/search-pc?api_key=51job&timestamp=1713696125&keyword=&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=1&pageNum=3&requestId=2a6b51f7426baa7d5995f3cd7a64c4a9&pageSize=20&source=1&accountId=&pageCode=sou%7Csou%7Csoulb"
// key = 'abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b'
//
// sign = CryptoJS.HmacSHA256(e, key).toString();
// console.log(sign)


function getSign(time, page) {
    e = "/api/job/search-pc?api_key=51job&timestamp=" + time + "&keyword=&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=1&pageNum=" + page + "&requestId=62c2413a6dc82c66aee1ae4f70b1a5ce&pageSize=20&source=1&accountId=&pageCode=sou%7Csou%7Csoulb"
    key = 'abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b'

    return CryptoJS.HmacSHA256(e, key).toString();

}