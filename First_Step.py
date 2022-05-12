for i in range(len(companies)):
    companies[i] = companies[i].capitalize()
    model[i] = model[i].capitalize()

list_helicopters = {'Company': companies, 'Model': model}
list_helicopters_pd = pd.DataFrame(list_helicopters)

new_helis = [['airbus','as355'],
             ['airbus','as145'],
             ['bell','b407'],
             ['bell','b429']] #inserindo nova lista

for y in range(len(new_helis)):

    list_helicopters_pd.index = list_helicopters_pd.index + 1
    list_helicopters_pd.loc[-1] = new_helis[y] #colocando nova lista

fix_cmp = list_helicopters_pd['Company'].tolist()
fix_mdl = list_helicopters_pd['Model'].tolist()

for x in range(len(fix_mdl)):
    fix_mdl[x] = fix_mdl[x].capitalize()
    fix_cmp[x] = fix_cmp[x].capitalize()

list_helicopters_pd['Company'] = fix_cmp
list_helicopters_pd['Model'] = fix_mdl

list_helicopters_pd = list_helicopters_pd.sort_values(by=['Company'],ascending=True)
list_helicopters_pd = list_helicopters_pd.reset_index(drop=True)

year = [2005, 2011, 2006, 2015, 2020, 1999, 2003]
list_helicopters_pd.insert(len(list_helicopters),'Year',year)

print(list_helicopters_pd)
## fazer graficos