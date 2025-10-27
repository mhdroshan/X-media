from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import UserModel
from Tags.models import TagRequest,following
from Posts.models import PostModel,PostImageModel,PostComment
# import easyocr # Removed EasyOCR functionality
from geopy.geocoders import Nominatim
from django.http import JsonResponse

# Create your views here.

def get_geolocation_data(request):
    if request.method == "POST":
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        if not latitude or not longitude:
            return JsonResponse({'success': False, 'error': 'Latitude and Longitude are required.'})

        try:
            geolocator = Nominatim(user_agent="X-media-Geolocation-App", timeout=10) # Increased timeout
            
            # Reverse geocode for country and city (more detailed)
            location = geolocator.reverse(f"{latitude}, {longitude}", exactly_one=True, addressdetails=True, namedetails=True)
            country = location.raw['address'].get('country', "Unknown") if location and 'address' in location.raw else "Unknown"
            detected_city = location.raw['address'].get('city') or location.raw['address'].get('town') or location.raw['address'].get('village') or "Unknown"
            detected_state = location.raw['address'].get('state', "Unknown")

            nearby_places = set() # Use a set for automatic uniqueness
            if detected_city != "Unknown":
                nearby_places.add(detected_city) # Always include the detected city
            
            # Extract other relevant nearby places from the raw address details
            address_components = location.raw.get('address', {})
            priority_types = ['city', 'town', 'village', 'county', 'suburb', 'neighbourhood'] # Exclude 'state' here
            
            for p_type in priority_types:
                if address_components.get(p_type):
                    place_name = address_components[p_type]
                    # Ensure place_name is not the country, detected city, or detected state
                    if place_name != country and place_name != detected_city and place_name != detected_state and place_name not in nearby_places:
                        nearby_places.add(place_name)
            
            nearby_places = list(nearby_places)

            # Ensure a minimum number of suggestions by adding more generic locations if needed
            if len(nearby_places) < 5:
                if location.raw['address'].get('county') and location.raw['address'].get('county') not in nearby_places:
                    nearby_places.append(location.raw['address']['county'])
                if location.raw['address'].get('state') and location.raw['address'].get('state') not in nearby_places:
                    nearby_places.append(location.raw['address']['state'])
                
                while len(nearby_places) < 5:
                    nearby_places.append(f"Generic Location {len(nearby_places) + 1}")

            # Limit to a reasonable number, e.g., 15-20, if too many unique places are found
            if len(nearby_places) > 20:
                nearby_places = nearby_places[:20]

            return JsonResponse({
                'success': True,
                'country': country,
                'state': detected_state, # Also return the detected state
                'city': detected_city, # Still return for potential display elsewhere if needed
                'nearby_cities': nearby_places # Return as a list
            })

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})

def userprofile(request):
    if request.session.has_key('userid'):
        userid = request.session['userid']
        users=UserModel.objects.get(id=userid)
        allMyPosts=PostModel.objects.filter(user_id=userid)
        foll_tags = following.objects.filter(user_id = userid).count()
        # com_count = PostComment.objects.filter(user = userid , post = allMyPosts).count()
        return render(request,"User/Profile.html",{'user':users , 'mypost':allMyPosts,'foll':foll_tags})
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
                return redirect("Posts:index")
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

def create_profile_step1_2(request):
    if request.method=="POST":
        name = request.POST.get("username")
        age = request.POST.get("userage")
        email = request.POST.get("useremail")
        phone = request.POST.get("userphone")

        user_data = {
            'name': name,
            'age': age,
            'email': email,
            'phone': phone
        }
        request.session['user_data'] = user_data
        return redirect('User:ver-pladd')
    return render(request,"User/createPro2.html",{})

# Removed verName function and EasyOCR functionality

def verPladd(request):
    if request.method=="POST":
        user_data = request.session.get('user_data', {})

        # Location data from createPro3.html POST
        user_data['country'] = request.POST.get("usercountry")
        user_data['state_display'] = request.POST.get("userstate_display") # The detected state
        user_data['detected_city'] = request.POST.get("userstate") # The detected city (from hidden input)
        user_data['longitude'] = request.POST.get("long")
        user_data['latitude'] = request.POST.get("lati")
        user_data['selected_nearby_city'] = request.POST.get("selected_nearby_city") # The user-selected nearby city

        request.session['user_data'] = user_data
        
        # Prepare context for createPro5.html
        context = {
            'name': user_data.get("name"),
            'age': user_data.get("age"),
            'email': user_data.get("email"),
            'phone': user_data.get("phone"),
            'country': user_data.get("country"),
            'state_display': user_data.get("state_display"),
            'detected_city': user_data.get("detected_city"),
            'longitude': user_data.get("longitude"),
            'latitude': user_data.get("latitude"),
            'selected_nearby_city': user_data.get("selected_nearby_city"),
        }

        return render(request,"User/createPro5.html",context)
    else:
        # Handle GET request by rendering the location input page
        return render(request, "User/createPro3.html", {})

def verDP(request):
    if request.method=="POST":

        t= UserModel()
        t.u_name = request.POST.get("username")
        t.u_age = request.POST.get("userage")
        t.u_email = request.POST.get("useremail")
        t.u_phone = request.POST.get("userphone")
        t.u_country = request.POST.get("usercountry")
        t.u_state = request.POST.get("userstate_display") # Detected State
        t.u_detected_city = request.POST.get("userstate") # Detected City (from hidden input)
        t.u_latitude = request.POST.get("lati")
        t.u_longitude = request.POST.get("long")
        t.u_selected_nearby_city = request.POST.get("selected_nearby_city")
        t.u_username = request.POST.get("nameuser")
        t.u_pass = request.POST.get("namepass")

        t.save()


        return redirect("/user/login")
        

