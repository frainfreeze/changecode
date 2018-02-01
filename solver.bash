echo first chalenge

curl --request POST --header "Content-type: application/json" -d '{"Teamname": "MenzaSimulator", "Password": "menzamajstori", "Members":[{"name": "Karlo", "surname": "Kegljević", "mail": "karlo.kegljevic@racunarstvo.hr"}, {"name": "Mislav", "surname": "Lalić", "mail": "mislav.lalic@racunarstvo.hr"}, {"name": "Rok", "surname": "Grgec", "mail": "rok.grgec@racunarstvo.hr"}, {"name": "Tomislav", "surname": "Kucar", "mail":"tomislav.kucar@racunarstvo.hr"}]}' 'http://52.233.158.172/change/api/hr/account/login'

echo second chalenge

curl --request POST --header "Content-type: application/json" -d '{"teamname": "MenzaSimulator","password":"menzamajstori"}  ' 'http://52.233.158.172/change/api/hr/account/login'

echo third chalenge

curl -X GET \
  http://52.233.158.172/change/api/hr/team/details/9 \
  -H 'x-authorization: TWVuemFTaW11bGF0b3I6Og==' \
  
echo and last one

curl -X GET \
  'http://52.233.158.172/change/api/hr/team/confirm?id=9&repository=https%3A%2F%2Fgithub.com%2Ffrainfreeze%2Fchangecode' \
  -H 'x-authorization: TWVuemFTaW11bGF0b3I6Og==' \
