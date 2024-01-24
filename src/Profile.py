import tornado.web

accountDatabase = {
    "alice": {
        "realname": "Alice Smith",
        "dateOfBirth": "Jan 1st",
        "email": "alice@example.com",
        "profpic": "Profile1.png"
    },
    "bob": {
        "realname": "Bob Jones",
        "dateOfBirth": "Dec. 31st",
        "email": "bob@bob.xyz",
        "profpic": "Profile2.png"
    },
    "carol": {
        "realname": "Carol Ling",
        "dateOfBirth": "Jul. 17th",
        "email": "carol@example.com",
        "profpic": "Profile3.png"
    },
    "dave": {
        "realname": "Dave N. Port",
        "dateOfBirth": "Mar.14th",
        "email": "dave@dave.dave",
        "profpic": "Profile4.png"
    }
}

class ProfileHandler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path       #ex: /profile/alice
        uname = p.split("/")[2]
        realname = accountDatabase[uname]["realname"]
        dob = accountDatabase[uname]["dateOfBirth"]
        email = accountDatabase[uname]["email"]
        profpic = accountDatabase[uname]["profpic"]

        self.render("profilepage.html",
                    realname = realname,
                    dob = dob,
                    email = email,
                    profpic = profpic
                    )

