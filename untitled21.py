# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GpuQGhGqTlaAagMNJoGvsREZiJ7QETMk
"""

def Salon_mashinalar(markasi):
  if markasi == "Gentra":
    return "Narxi=165mln "
  elif  markasi == "Onix":
    return "Narxi=160mln"
  elif  markasi == "Cobalt":
    return "Narxi=155mln"
  elif  markasi == "Nexia 3":
    return "Narxi=140mln"
  elif  markasi == "Captiva 5":
    return "Narxi=284mln"
  elif  markasi == "Labo":
    return "Narxi=84mln"
  elif  markasi == "Spark":
    return "Narxi=130mln"
  elif  markasi == "Malibu 2":
    return "Narxi=419mln"
  elif  markasi == "Damas Deluxe":
    return "Narxi=84mln"
  else:
    return "Bu markalarga shartnoma salonimizda mavjud emas"
markasi=input("Markasini kiriting:")
natija=Salon_mashinalar(markasi)
print(natija)

def kasallik_tashxisi(belgi):
  if belgi == "isitma":
    return "Parasetamol iching "
  elif belgi == "bosh og'rig'i":
    return "Trimol iching"
  elif belgi == "Qon bosimining oshishi":
      return "Adipin iching"
  elif belgi=="Tish og'rig'i":
        return "Kyupen iching"
  elif belgi=="Oyoq og'rig'i":
          return "Diklofenak surting"
  elif belgi == "Ko'z og'rig'i":
         return "Farmadeksdan 2 tomchi tomizing"
  if belgi == "Tomoq og'rig'i":
          return "Mukaltin iching"
  if belgi == "yengil kuyish":
    return "Tish pastasi surting"
  if belgi == "grip":
    return "Taylol hot iching"
  if belgi == "Qorin og'rig'i":
    return "Mezim iching"
  else:
    return "Shifokorga murojaat qiling"
belgi=input("Kasallikni kiriting:")
natija=kasallik_tashxisi(belgi)
print(natija)