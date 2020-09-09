from django.shortcuts import render

# pylint: disable=unused-variable
# pylint: enable=too-many-lines

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_requests = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=FB8713A4-7780-42D7-9B2D-AF57A058FF1B")

        try:
            api = json.loads(api_requests.content)
        except Exception as e:
            api = "Error..."

        colors = []
        if api == []:
            return render(request, 'home.html', { 'zipcode' : zipcode })
        else:
            for x in api:
                # colors.append(x)
                if x['Category']['Name'] == "Good":
                    # colors[x] = "good"
                    colors.append("good")
                elif x['Category']['Name'] == "Moderate":
                    # colors[x] = "moderate"
                    colors.append("moderate")
                elif x['Category']['Name'] == "Unsafe For Sensitive Groups":
                    # colors[x] = "usg"
                    colors.append("usg")
                elif x['Category']['Name'] == "Unhealthy":
                    # colors[x] = "unhealthy"
                    colors.append("unhealthy")
                elif x['Category']['Name'] == "Very Unhealthy":
                    # colors[x] = "veryunhealthy"
                    colors.append("veryunhealthy")
                else:
                    colors.append("hazardous")
            return render(request, 'home.html', { 'api': api, 'cat_col1' : colors[0], 'cat_col2' : colors[1] })
    else:

        api_requests = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=94080&distance=5&API_KEY=FB8713A4-7780-42D7-9B2D-AF57A058FF1B")

        try:
            api = json.loads(api_requests.content)
        except Exception as e:
            api = "Error..."

        colors = []
        for x in api:
            if x['Category']['Name'] == "Good":
                colors.append("good")
            elif x['Category']['Name'] == "Moderate":
                colors.append("moderate")
            elif x['Category']['Name'] == "Unsafe For Sensitive Groups":
                colors.append("usg")
            elif x['Category']['Name'] == "Unhealthy":
                colors.append("unhealthy")
            elif x['Category']['Name'] == "Very Unhealthy":
                colors.append("veryunhealthy")
            else:
                colors.append("hazardous")

        return render(request, 'home.html', { 'api': api, 'cat_col1' : colors[0], 'cat_col2' : colors[1] })

def about(request):
    return render(request, 'about.html', {})