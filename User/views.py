from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import UserModel,tempProof
from Tags.models import TagRequest
from Posts.models import PostModel,PostImageModel,PostComment
import easyocr
from geopy.geocoders import Nominatim

# Create your views here.

def userprofile(request):
    if request.session.has_key('userid'):
        userid = request.session['userid']
        users=UserModel.objects.get(id=userid)
        allMyPosts=PostModel.objects.filter(user_id=userid)
        # com_count = PostComment.objects.filter(user = userid , post = allMyPosts).count()
        return render(request,"User/Profile.html",{'user':users , 'mypost':allMyPosts})
    else:
        return redirect("/user/login")

def changePrivacy(request,id):
    user  = UserModel.objects.get(id=id)
    radio = request.POST.get("anontype")
    if request.method == 'POST':
        if radio == '0':
            
            user.u_security ='0'
            user.save()
            return redirect('User:profile')
            
        elif radio =='1':
            user.u_security = '1'
            user.save()
            return redirect('User:profile')



def deletePost(request,id):
    if request.session.has_key('userid'):
        post =  PostModel.objects.get(id=id)
        post.delete()
        return redirect("/user/profile")

    else:
        return redirect("/user/login")


def moreimage(request,id):
    userid = request.session['userid']
    users=UserModel.objects.get(id=userid)
    allMyPosts=PostModel.objects.filter(user_id=userid)
    if request.method == 'POST' and request.FILES:
        postImagesObj=PostImageModel()
        # postImagesObj.img_title= "image-title"
        postImagesObj.img_title= request.POST.get("imagetitle")
        postImagesObj.post_image= request.FILES.get("postImage")
        postObj=PostModel.objects.get(id=id)
        postImagesObj.post=postObj
        # return HttpResponse(postImagesObj)
        postImagesObj.save()
        return render(request,"User/Profile.html",{'flag':1 ,'user':users,'mypost':allMyPosts})

    else:
        return render(request,"User/Profile.html",{'user':users,'mypost':allMyPosts})
    
    
def login(request):
    if request.session.has_key('userid'):
        return redirect("/user/profile")
    else:
        if request.method=="POST":
            userLoged=UserModel.objects.filter(u_username=request.POST.get("username"),u_pass=request.POST.get("password")).count()
            if userLoged>0:
                user=get_object_or_404(UserModel, u_username=request.POST.get("username"),u_pass=request.POST.get("password"))
                request.session["userid"]=user.id
                return redirect("/")
            else:
                return render(request,"user/login.html",{'fail':1})
        return render(request,"user/login.html",{})



def logout(request):
    request.session.flush()
    return redirect("/user/login")


def tagreq(request):
    
    if request.session.has_key('userid'):
        
        if request.method=="POST":
            t=TagRequest()
            t.tr_title=request.POST.get("tagtitle")
            t.tr_content=request.POST.get("tagdesc")
            t.tr_c=request.POST.get("tagcountry")
            t.tr_s=request.POST.get("tagstate")
            t.tr_p=request.POST.get("tagplace")
            t.tr_type=request.POST.get("loctype")

            userObject=UserModel.objects.get(id=request.session["userid"])
            t.user_id=userObject
            
            

            t.save()
            return render(request,"user/tagRequest.html",{'flag':1})
        return render(request,"user/tagRequest.html",{})

    else:
        return redirect("/user/login")

# create profile

def create(request):
    return render(request,"User/createPro.html",{})




def verName(request):
    # return render(request,"User/createPro2.html",{})

    
    if request.method=="POST" and request.FILES:
        t = tempProof()
        name = request.POST.get("username")
        namestr = str(name).lower()
        uname = namestr.replace(" ", "")


        t.proof = request.FILES.get("nameproof")
        t.name = request.POST.get("username")
        t.save()
        reader = easyocr.Reader(['en'])
        result = reader.readtext(t.proof.path,detail=0,paragraph=True)
        strproof = str(result)
        proofid="".join(c for c in strproof if c.isalpha()).lower()
        if uname not in proofid:
            return render(request,"User/createPro.html",{'fail':1})

        else:
            return render(request,"User/createPro2.html",{'name':name})


def verOther(request):
    if request.method=="POST":
        name = request.POST.get("username")
        age = request.POST.get("userage")
        email = request.POST.get("useremail")
        phone = request.POST.get("userphone")

        context = {
            'name':name,
            'age':age,
            'email':email,
            'phone':phone
        }
        # return HttpResponse(context.name)

        return render(request,"User/createPro3.html",context)



def verLocation(request):
    # return render(request,"User/createPro4.html",{})
  
    if request.method=="POST":
        name = request.POST.get("username")
        age = request.POST.get("userage")
        email = request.POST.get("useremail")
        phone = request.POST.get("userphone")
        
        
        


        t = tempProof()
        country = request.POST.get("usercountry")
        constr = str(country).lower()
        cont = constr.replace(" ", "")

        state = request.POST.get("userstate")
        statestr = str(state).lower()
        stat = statestr.replace(" ", "")

        t.proof = request.FILES.get("locationproof")
        t.name = request.POST.get("username")
        t.save()

        reader = easyocr.Reader(['en'])
        result = reader.readtext(t.proof.path,detail=0,paragraph=True)
        strproof = str(result)
        proofid="".join(c for c in strproof if c.isalpha()).lower()

        context = {
            'name':name,
            'age':age,
            'email':email,
            'phone':phone,
            'country':country,
            'state':state,
            
        }
        



        if cont not in proofid or stat not in proofid:
            return render(request,"User/createPro3.html",{'fail':1})

        else:
            return render(request,"User/createPro4.html",context)



def verPlaceget(request):
    # return render(request,"User/createPro5.html",{})
    if request.method=="POST":

        name = request.POST.get("username")
        age = request.POST.get("userage")
        email = request.POST.get("useremail")
        phone = request.POST.get("userphone")
        country = request.POST.get("usercountry")
        state = request.POST.get("userstate")
        place = request.POST.get("userplace")
       
        long = request.POST.get("long")
        lati = request.POST.get("lati")
        

        geolocator = Nominatim(user_agent="geoapiExercises")
       
        # Latitude = "11.288575999999999"
        # Longitude = "76.251136"
    
        location = geolocator.reverse(lati+","+long ,timeout=None)
        address = location.raw['address']
        town = address.get('town')
        city = address.get('city')
        village = address.get('village')
        if town:
            return render(request,"User/createPro4.html",{
                
                'name':name,
                'age':age,
                'email':email,
                'phone':phone,
                'country':country,
                'state':state,
                'place':town,
                })
        elif city:
            return render(request,"User/createPro4.html",{
                
                'name':name,
                'age':age,
                'email':email,
                'phone':phone,
                'country':country,
                'state':state,
                'place':city,
                })
        elif village:
            return render(request,"User/createPro4.html",{
                
                'name':name,
                'age':age,
                'email':email,
                'phone':phone,
                'country':country,
                'state':state,
                'place':village,
            
            })
        else:
            return render(request,"User/createPro4.html",{
                'flag':1,
                'name':name,
                'age':age,
                'email':email,
                'phone':phone,
                'country':country,
                'state':state,
                'place':0,} )
        
        


def verPladd(request):
    if request.method=="POST":
        name = request.POST.get("username")
        age = request.POST.get("userage")
        email = request.POST.get("useremail")
        phone = request.POST.get("userphone")
        country = request.POST.get("usercountry")
        state = request.POST.get("userstate")
        place = request.POST.get("userplace")
        context = {
            'name':name,
            'age':age,
            'email':email,
            'phone':phone,
            'country':country,
            'state':state,
            'place':place,
            
        }

        return render(request,"User/createPro5.html",context)

def verDP(request):
    if request.method=="POST" and request.FILES:

        t= UserModel()
        t.u_name = request.POST.get("username")
        t.u_age = request.POST.get("userage")
        t.u_email = request.POST.get("useremail")
        t.u_phone = request.POST.get("userphone")
        t.u_country = request.POST.get("usercountry")
        t.u_state = request.POST.get("userstate")
        t.u_place = request.POST.get("userplace")
        t.u_username = request.POST.get("nameuser")
        t.u_pass = request.POST.get("namepass")
        t.u_pic = request.FILES.get("userpic")

        t.save()


        return redirect("/user/login")
        

