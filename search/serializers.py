from rest_framework import serializers

class SearchSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Corpus
		fields = '__all__'
