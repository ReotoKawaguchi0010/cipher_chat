"use strict";
class GetJson extends XMLHttpRequest {
    constructor() {
        super();
        this.host = location.pathname;
        this.url = '/text.json' + this.host;
        this.open('GET', this.url, true);
        this.responseType = 'json';
        this.setRequestHeader('content-type', 'application/json');
        this.send();
    }
    getJson() {
        this.addEventListener('load', function () {
            let get_json = this.response;
            for (let i in get_json) {
                let elements = document.querySelectorAll('.chat_text');
                const $newText = document.createElement('div');
                let $test = document.createTextNode(get_json[i]['text']);
                $newText.appendChild($test);
                elements.forEach(element => {
                    element.appendChild($newText);
                });
            }
            return get_json;
        });
    }
    ;
}
const sendJson = (content) => {
    const ajax = new XMLHttpRequest();
    ajax.open('POST', '/model', true);
    ajax.setRequestHeader('content-type', 'application/json');
    ajax.setRequestHeader('data-type', 'json');
    ajax.send(JSON.stringify(content));
};
const createJson = (letters, toJapaneseLetters) => {
    let json = {
        'text': letters,
        'page_id': location.pathname.replace('/', ''),
        'to_japanese_letters': toJapaneseLetters,
    };
    return json;
};
const textJudgment = (japaneseLetters) => {
    for (let i = 0; i < japaneseLetters.length; i++) {
        if (!japaneseLetters[i].match(/[a-zA-Z]/)) {
            return true;
            break;
        }
    }
    return false;
};
function main() {
    let req = new GetJson();
    let test = document.getElementsByTagName('input');
    let airList = [];
    req.getJson();
    test[2].addEventListener('keydown', (event) => {
        if (event.key == 'Backspace') {
            airList.pop();
        }
        else if (event.key.length === 1) {
            airList.push(event.key);
        }
    });
    document.addEventListener('submit', () => {
        let toJapaneseLetters = airList.join('');
        let letters = document.querySelectorAll('#test_text')[0].value;
        let data = createJson(letters, toJapaneseLetters);
        sendJson(data);
    });
}
;
main();
