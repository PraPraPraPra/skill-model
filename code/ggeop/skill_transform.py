def skill_transform(skill, remove_stopwords = True):
    
    skill = skill.replace("_", " ").split()
    skill = " ".join([sk for sk in skill if sk])
    
    skill = re.sub(r"\(.*\)", "", skill)
    skill = skill.replace("-", "") \
        .replace(".", "") \
        .replace(",", "") \
        .replace("-", "") \
        .replace(":", "") \
        .replace("(", "") \
        .replace(")", "") \
        .replace(u"åá", "") \
        .replace(u"&", "and") \
        .replace(" js", "js") \
        .replace("-js", "js") \
        .replace("_js", "js") \
        .replace("java script", "js") 
    
    skill = skill.lower()
    
    # Special cases replace
    special_case = {}
    special_case["javascript"] = [ "js", "java script", "javascripts", "java scrip" ]
    special_case["wireframe"] = [ "wireframes", "wire frame", "wire frames", "wire-frame", "wirefram", "wire fram", "wireframing" ]
    special_case["oop"] = [  "object oriented", "object oriented programming", ]
    special_case["ood"] = [ "object oriented design", ]
    special_case["olap"] = [ "online analytical processing",  ]
    special_case["ecommerce"] = [ "e commerce",  ]
    special_case["consultant"] = [ "consulting",  ]
    special_case["ux"] = [ "user experience", "web user experience design", "user experience design", "ux designer", "user experience/ux" ]
    special_case["html5"] = [ "html 5",  ]
    special_case["j2ee"] = [ "jee",  ]
    special_case["osx"] = [ "mac os x", "os x" ]
    special_case["senior"] = [ "sr" ]
    special_case["qa"] = [ "quality",  ]
    special_case["bigdata"] = [ "big data"]
    special_case["webservice"] = [ "webservices", "website", "webapps" ]
    special_case["xml"] = [ "xml file", "xml schemas", "xml web service" ]
    special_case["nlp"] = [ "natural language process", "natural language", "nltk" ]
    special_case["aws"] = [ "amazon web service"]
    special_case["java ee"] = [ "java"]

    
    for root_skill in special_case:
        if skill in special_case[root_skill]:
            skill = root_skill
    
    # Special case regex
    special_case_regex = {
        r'^angular.*$': 'angularjs',
        r'^node.*$': 'nodejs',
        r'^(.*)[_\s]js$': '\\1js',
        r'^(.*) js$': '\\1js',
        r'^(.*) (and|or).*$': '\\1',
    }
    for regex_rule in special_case_regex:
        after_skill = re.sub(regex_rule, special_case_regex[regex_rule], skill)
        if after_skill != skill:
            skill = after_skill
            break
    
    # Stem
    if len(skill) > 2:
        skill_after = skill.split(" ")
        skill_after = [wordnet_lemmatizer.lemmatize(sk, pos="v") for sk in skill_after]
        skill_after = " ".join(skill_after)
        skill = skill_after
    
    # skill stopwords 
    if remove_stopwords:
        skill_stopwords = [ "app", "touch", "the", "application", "programming", "program", "design"
                           "developer", "framework", "development", "programmer", "technologies",
                          "advance", "core"]
        skill_after = skill.split(" ")
        skill = " ".join([ sk for sk in skill_after if sk not in skill_stopwords ])
    
    skill = skill.lower().strip().replace(" ", "_")
    skill = re.sub(' +',' ', skill)
    
    # NOTE: replace js tail
    skill = re.sub('js$','', skill)
    
    return skill