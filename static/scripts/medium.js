var stories = [];


function init(){
    var url = 'https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@alphaxsalt';

    fetch(url)
    .then((res) => res.json())
    .then((data) => {
        // Fillter the array
        const res = data.items //This is an array with the content. No feed, no info about author etc..
        const posts = res.filter(item => item.categories.length > 0) // That's the main trick* !

        stories = posts
        
        //console.log(stories)
        
        var story = ""

        if(stories.length > 0){
            stories.map(t => {
                story += `<div class="mix col-md-6 col-lg-4 rened">
                            <a href=${t.link} class="portfolio-item pi-style2 set-bg" style="background-image: url(${t.thumbnail}); border-radius: 5%">
                                <div class="pi-inner">
                                    <h2>+ Read</h2>
                                </div>						
                            </a>
                            <div class="portfolio-meta">
                                <h2>${t.title}</h2>
                            </div>
                        </div>`;
            })

            //insert
            document.getElementById("story_section").innerHTML = story;
        }
    }).catch(err => {
        console.log(err)
    })
}



init()