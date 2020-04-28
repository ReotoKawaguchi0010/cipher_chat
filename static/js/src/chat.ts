class GetJson extends XMLHttpRequest{
    host: string= location.pathname;
    url: string = '/text.json' + this.host;
    constructor() {
        super();
        this.open('GET', this.url, true);
        this.responseType = 'json';
        this.setRequestHeader('content-type', 'application/json');
        this.send();
    }

    public getJson(){
        this.addEventListener('load', function(){
            let get_json = this.response;
            let username = document.getElementsByClassName('username')[0].textContent;

            for (let i in get_json){
                let elements = document.querySelectorAll<HTMLDivElement>('.chat_text');
                let $newText: HTMLDivElement = document.createElement('div');
                let $test = document.createTextNode(get_json[i]['text']);
                if (get_json[i]['username'] == username){
                    $newText.className = 'now_user'
                }else {
                    $newText.className = 'else_user'
                }
                $newText.appendChild($test);

                elements.forEach(element => {
                    element.appendChild($newText);
                });
            }
            return get_json
        });
    };
}

const sendJson = (content: object) => {
    const ajax = new XMLHttpRequest();
    ajax.open('POST', '/model', true);
    ajax.setRequestHeader('content-type', 'application/json');
    ajax.setRequestHeader('data-type', 'json');
    ajax.send(JSON.stringify(content));
};

const createJson = (letters: string, toJapaneseLetters: string) =>{
    let json: object = {
        'text' : letters,
        'page_id': location.pathname.replace('/', ''),
        'to_japanese_letters': toJapaneseLetters,
    };
    return json
};

const textJudgment = (japaneseLetters: string) => {
    for (let i=0; i<japaneseLetters.length; i++){
        if (!japaneseLetters[i].match(/[a-zA-Z]/)){
            return true;
            break
        }
    }
    return false
};

function main(){
    let req = new GetJson();
    let test = document.getElementsByTagName('input');
    let airList: string[] = [];
    console.log();
    req.getJson();
    test[2].addEventListener('keydown', (event) => {
        if(event.key == 'Backspace'){
            airList.pop()
        }else if(event.key.length === 1){
            airList.push(event.key);
        }
    });

    document.addEventListener('submit', () => {
        let toJapaneseLetters: string = airList.join('');
        let letters: string = document.querySelectorAll<HTMLInputElement>('#test_text')[0].value;
        let data: object = createJson(letters, toJapaneseLetters);
        sendJson(data);
    })
};

main();