var isPalindrome = function (s) {
    s = s.toLowerCase().replace(/[^a-z\d]/g, '');
  
    let start = 0
    let end = s.length - 1

    if (s.length === 0) {
        return true
    }
    while (start < end) {
        if (s[start] !== s[end]) {
            return false
        }
            start++
            end--
    }
    return true

};

console.log(isPalindrome("A man, a plan, a canal: Panama"))