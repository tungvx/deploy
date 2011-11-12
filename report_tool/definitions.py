def get_hs(school,class_id):
    p = Pupil.objects.filter(school_id = school, class_id=class_id)
    for i in p:
        print p.first_nane