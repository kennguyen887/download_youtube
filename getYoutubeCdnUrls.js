const ytdl = require('ytdl-core');

async function getVideoInfo(id) {
    var videoInfo = await ytdl.getInfo(id);
    var hd;
    try { hd = videoInfo.formats.find(x => x.itag == 22).url; } catch (e) {}
    var sd = videoInfo.formats.find(x => x.itag == 18).url;
    var audio = videoInfo.formats.find(x => x.itag == 140).url;
    var formats = { hd, sd, audio };
    return formats;
}

getVideoInfo("JpGxvSejVDE")
.then(results => console.log(results))
