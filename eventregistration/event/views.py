from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
 
from .models import *
from datetime import datetime    

@api_view(['POST'])

def create_event(request):
   
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    if request.user.is_authenticated:
        
        user=request.user
        title=request.data['title']
        description=request.data['description']
        date=request.data['date']
        slots=request.data['slots']
        
    

        date_object = datetime.strptime(date, "%d-%m-%Y").date()
        time=request.data['time']
        time_object = datetime.strptime(time, '%H:%M').time()
        print(date_object , time_object)
        location=request.data['location']
        event=Event.objects.create(title=title,description=description,date=date_object,time=time_object,location=location,slots=slots,event_creator=user)
        event.save()
        return Response({"success":"event created successfully"})

        


@api_view(['POST'])

def register_event(request,eventid):

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    if request.user.is_authenticated:
        
        user=request.user
        userid=request.user.id
        event=Event.objects.get(id=eventid)
        slots=event.slots
        if slots>0:
            check=Registered_events.objects.filter(event_id=eventid,participants_id=userid)
            if check:
                return Response({"success":"Already registerd for event"})
                
            else:
                reg_event=Registered_events.objects.create(event=event,participants=user)
                cur_slots=slots
                cur_slots-=1
                event.slots=cur_slots
                event.save()
                reg_event.save()

                return Response({"success":"registered for event succesfully"})
         

@api_view(['POST'])

def unregister_event(request,eventid):

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    if request.user.is_authenticated:
        
        user=request.user
        userid=request.user.id
        event=Event.objects.get(id=eventid)

        if event:
            check=Registered_events.objects.filter(participants_id=userid,event_id=eventid)
            if check:
                cur_slot=event.slots
                check.delete()
                cur_slot+=1
                event.slots=cur_slot
                event.save()
                return Response({"success":"unregistered"})
                
            else:

                return Response({"error":"You are not registered"})

         
        


@api_view(['GET'])

def event_list(request):

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    if request.user.is_authenticated:
        
        user=request.user
        userid=request.user.id
        
        
        reg_event=Registered_events.objects.filter(participants_id=userid)
        if reg_event:
            event_idlist=set()
            for id in reg_event:
                event_idlist.add(id.event_id)
            print(event_idlist)
            eventdata=[]
           
            event=Event.objects.exclude(id__in=event_idlist)

                

            for data in event:
                    creator_id=data.event_creator_id
                    user=User.objects.get(id=creator_id)
                    
                    eventdata.append({
                        "event_id":data.id,
                        "event_title":data.title,
                        "event_description":data.description,
                        "event_date":data.date,
                        "event_time":data.time,
                        "location":data.location,
                        "slots":data.slots,
                        "organizer":user.first_name


                    })
                    

            return Response(
                eventdata
            )
        else:
            event=Event.objects.all()
            eventdata=[]
            for data in event:
                    creator_id=data.event_creator_id
                    user=User.objects.get(id=creator_id)
                    eventdata.append({
                        "event_id":data.id,
                        "event_title":data.title,
                        "event_description":data.description,
                        "event_date":data.date,
                        "event_time":data.time,
                        "location":data.location,
                        "slots":data.slots,
                        "organizer":user.first_name


                    })
            return Response(
                eventdata
            )
    else:
        return Response({"error":"you are not authorized"})


@api_view(['GET'])

def reg_event_list(request):

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    if request.user.is_authenticated:
        
        user=request.user
        userid=request.user.id
        
        
        reg_event=Registered_events.objects.filter(participants_id=userid)
        if reg_event:
            event_idlist=set()
            for id in reg_event:
                event_idlist.add(id.event_id)
            
            eventdata=[]

            for event_id in event_idlist:
                print(event_id)
                event=Event.objects.filter(id=event_id)

                

                for data in event:
                    creator_id=data.event_creator_id
                    user=User.objects.get(id=creator_id)
                    eventdata.append({
                        "event_id":data.id,
                        "event_title":data.title,
                        "event_description":data.description,
                        "event_date":data.date,
                        "event_time":data.time,
                        "location":data.location,
                        "slots":data.slots,
                        "organizer":user.first_name


                    })

            return Response(
                eventdata
            )
        else:
            return Response({
                "error":"you have not registred for any events"
            })


@api_view(['GET'])

def all_event_list(request):

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    if request.user.is_authenticated:
        
        user=request.user
        userid=request.user.id
        
        
        
        event=Event.objects.all()
        eventdata=[]
        if event:        

            for data in event:
                    creator_id=data.event_creator_id
                    user=User.objects.get(id=creator_id)
                    eventdata.append({
                        "event_id":data.id,
                        "event_title":data.title,
                        "event_description":data.description,
                        "event_date":data.date,
                        "event_time":data.time,
                        "location":data.location,
                        "slots":data.slots,
                        "organizer":user.first_name


                    })

            return Response(
                eventdata
            )
        else:
            return Response({
                "error":"There is no event yet"
            })
