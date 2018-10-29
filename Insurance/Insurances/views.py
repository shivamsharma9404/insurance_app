from rest_framework import  status
from .serializers import InsuranceSerializers,TransactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Insurance
from rest_framework.generics import RetrieveUpdateDestroyAPIView



class createInsurance(APIView):
     def post(self,request):
        print(request.data)
        data_old ={'cust_id': request.data.get('cust_id'),'insurance_type': request.data.get('insurance_type'),'total_insurance':request.data.get('total_insurance')}
        print(data_old)
        serializer = InsuranceSerializers(data=request.data)
        if serializer.is_valid():
            insurance = serializer.save()
            print(insurance)
            new_data = {'cust_id': request.data.get('cust_id'),'insurance': insurance.pk, 'Insurance_accnt': request.data.get('total_insurance')}
            print(new_data)
            t_serializer = TransactionSerializer(data=new_data)
            if t_serializer.is_valid():
                print("hi")
                transaction =t_serializer.save()
                print("hi")
                return Response(status=status.HTTP_201_CREATED)
            return Response (serializer.data, status=status.HTTP_201_CREATED)
     def get(self,request):
         return Response("hi")

class InsuranceList(APIView):
        def get(self,request):
          Insurnc = Insurance.object.all()
          serializer = InsuranceSerializers(Insurnc,many=True).data
          return Response(serializer)


class InsuranceDetail(RetrieveUpdateDestroyAPIView):
    queryset =  Insurance.object.all()
    serializer_class =  InsuranceSerializers


