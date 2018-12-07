results= [{"id":1,"first_name":"Orbadiah","last_name":"Taberer","math":34,"english":59,"french":97},{"id":2,"first_name":"Olivier","last_name":"Gianetti","math":60,"english":54,"french":93},{"id":3,"first_name":"Robinson","last_name":"Kybird","math":68,"english":28,"french":59},{"id":4,"first_name":"Gerladina","last_name":"Linstead","math":24,"english":75,"french":59},{"id":5,"first_name":"Morton","last_name":"Cozby","math":100,"english":72,"french":24},{"id":6,"first_name":"Ann","last_name":"Goodsell","math":73,"english":42,"french":20},{"id":7,"first_name":"Josey","last_name":"Bayliss","math":73,"english":26,"french":46},{"id":8,"first_name":"Terence","last_name":"Giffard","math":72,"english":32,"french":64},{"id":9,"first_name":"Brittaney","last_name":"Marrington","math":38,"english":35,"french":33},{"id":10,"first_name":"Betti","last_name":"Osban","math":37,"english":80,"french":66},{"id":11,"first_name":"Ella","last_name":"Ingold","math":85,"english":23,"french":77},{"id":12,"first_name":"Emanuel","last_name":"Nisot","math":65,"english":82,"french":59},{"id":13,"first_name":"Laurent","last_name":"Moyers","math":56,"english":49,"french":34},{"id":14,"first_name":"Jakob","last_name":"Tallant","math":75,"english":51,"french":63},{"id":15,"first_name":"Lucy","last_name":"Priver","math":35,"english":50,"french":20},{"id":16,"first_name":"Lefty","last_name":"Pund","math":79,"english":32,"french":30},{"id":17,"first_name":"Carena","last_name":"Durban","math":30,"english":81,"french":22},{"id":18,"first_name":"Lisbeth","last_name":"Romanetti","math":74,"english":49,"french":96},{"id":19,"first_name":"Gussie","last_name":"Laundon","math":87,"english":67,"french":95},{"id":20,"first_name":"Devland","last_name":"Scowcroft","math":37,"english":49,"french":60},{"id":21,"first_name":"Magdalena","last_name":"Hunnicutt","math":43,"english":84,"french":58},{"id":22,"first_name":"Kamilah","last_name":"Dulwich","math":75,"english":78,"french":77},{"id":23,"first_name":"Catina","last_name":"Robertazzi","math":20,"english":61,"french":28},{"id":24,"first_name":"Anetta","last_name":"Jankowski","math":87,"english":62,"french":82},{"id":25,"first_name":"Cherry","last_name":"Enefer","math":50,"english":95,"french":54},{"id":26,"first_name":"Danyette","last_name":"Davenhill","math":85,"english":61,"french":46},{"id":27,"first_name":"Olenolin","last_name":"Borley","math":84,"english":57,"french":30},{"id":28,"first_name":"Liane","last_name":"Kalberer","math":34,"english":93,"french":40},{"id":29,"first_name":"Brit","last_name":"Surplice","math":41,"english":29,"french":37},{"id":30,"first_name":"Emmery","last_name":"Pittock","math":44,"english":24,"french":53},{"id":31,"first_name":"Jaclyn","last_name":"Souster","math":100,"english":35,"french":80},{"id":32,"first_name":"Zeke","last_name":"Mertin","math":99,"english":59,"french":99},{"id":33,"first_name":"Nikki","last_name":"Skeete","math":65,"english":76,"french":85},{"id":34,"first_name":"Ora","last_name":"Jolley","math":87,"english":36,"french":96},{"id":35,"first_name":"Seward","last_name":"Fanshawe","math":99,"english":25,"french":25},{"id":36,"first_name":"Dierdre","last_name":"Wooland","math":38,"english":90,"french":85},{"id":37,"first_name":"Humfried","last_name":"Maber","math":97,"english":74,"french":88},{"id":38,"first_name":"Obie","last_name":"Adamson","math":82,"english":69,"french":32},{"id":39,"first_name":"Gertrud","last_name":"Plant","math":62,"english":50,"french":97},{"id":40,"first_name":"Celia","last_name":"Faithfull","math":60,"english":23,"french":90},{"id":41,"first_name":"Esther","last_name":"Hurworth","math":43,"english":58,"french":98},{"id":42,"first_name":"Clarke","last_name":"Hitzschke","math":32,"english":100,"french":70},{"id":43,"first_name":"Saunder","last_name":"Balke","math":84,"english":97,"french":63},{"id":44,"first_name":"Gerhard","last_name":"O'Lynn","math":68,"english":97,"french":76},{"id":45,"first_name":"Remy","last_name":"Bikker","math":88,"english":57,"french":88},{"id":46,"first_name":"Korney","last_name":"Chesworth","math":40,"english":68,"french":96},{"id":47,"first_name":"Felipe","last_name":"Mashal","math":71,"english":57,"french":93},{"id":48,"first_name":"Fairlie","last_name":"Phalp","math":26,"english":76,"french":53},{"id":49,"first_name":"Ham","last_name":"Fidgeon","math":66,"english":61,"french":43},{"id":50,"first_name":"Arlie","last_name":"Readshall","math":51,"english":79,"french":37}]

# print all the scores

# for person in results:
#     print(person["first_name"])
#     print(person["last_name"])
#     print(person["english"])
#     print(person["math"])
#     print(person["french"])
#     print("------------------------------------------")

# first_name and english score for above 50
size = len(results)
# total = 0
#
# for results in results:
#     total += results["french"] + results["math"] + results["english"]
#
# print("Total sum of french is", total)
# print("AVG is", total/size)

# for result in results:
#     total = result["french"] + result["math"] + result["english"]
#     result["total"] = total
#
# print(results)
#
# from operator import itemgetter
# sorted_results = sorted(results, key=itemgetter("total"), reverse=True)
#
# print(sorted_results)
# for index in range(0,10):
#     res = sorted_results[index]
#     print(res["first_name"])
#     print(res["total"])
#     print("------------------------------------------------------------------")



# last_name and score in french if the score is an even number
print(11%2) #Modulus

for item in results:
    if item["french"] % 2 == 0:
        print(item["first_name"])
        print(item["french"])

for Odd in results:
    if Odd ["french"] % 2 == 1:
        print(Odd["first_name"])
        print(Odd["french"])

