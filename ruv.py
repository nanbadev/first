from random import randint
from IPython.display import display, Javascript, HTML
class RecordUV:
    builted=False
    def __init__(self):
        if not RecordUV.builted:
            self.setUpTheGolabalJs()
            RecordUV.builted=True
    def setUpTheGolabalJs(self):
        js="""
        if(!window['recorder'])
        window['recorder']=(id)=>new Promise(async resolve=>{
            var stream = await navigator.mediaDevices.getUserMedia({ audio: true })
            window['rec_'+id] = new MediaRecorder(stream)
            var chunks = []
            window['rec_'+id].ondataavailable = e => chunks.push(e.data)
            window['rec_'+id].start()
            window['rec_'+id].onstop = async ()=>{
                console.log('clisti')
                var blob = new Blob(chunks)
                var blobUrl = URL.createObjectURL(blob);
                document.getElementById('audio_'+id).setAttribute('src',blobUrl)
                resolve()
            }
        })
        if(!window['stoprecord'])
        window['stoprecord']=(id)=>{
            window['rec_'+id].stop()
            return;
        }
        """
        return display(Javascript(js))
    def getRecorder(self):
        idd=str(randint(100000, 999999))
        hl=f"<button id='start_{idd}'"+f" onclick='recorder({idd})'>Start</button>"
        hl+=f"<button id='stop_{idd}'"+f" onclick='stoprecord({idd})'>Stop</button>"
        hl+=f"<audio controls id='audio_{idd}'"+f"</audio>"
        return display(HTML(hl))