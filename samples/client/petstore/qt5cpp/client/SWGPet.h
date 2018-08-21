/**
 * Swagger Petstore
 * This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.
 *
 * OpenAPI spec version: 1.0.0
 * Contact: apiteam@swagger.io
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

/*
 * SWGPet.h
 * 
 * A pet for sale in the pet store
 */

#ifndef SWGPet_H_
#define SWGPet_H_

#include <QJsonObject>


#include "SWGCategory.h"
#include "SWGTag.h"
#include <QList>
#include <QString>

#include "SWGObject.h"

namespace Swagger {

class SWGPet: public SWGObject {
public:
    SWGPet();
    SWGPet(QString* json);
    virtual ~SWGPet();
    void init();
    void cleanup();

    QString asJson ();
    QJsonObject* asJsonObject();
    void fromJsonObject(QJsonObject &json);
    SWGPet* fromJson(QString &jsonString);

    qint64 getId();
    void setId(qint64 id);

    SWGCategory* getCategory();
    void setCategory(SWGCategory* category);

    QString* getName();
    void setName(QString* name);

    QList<QString*>* getPhotoUrls();
    void setPhotoUrls(QList<QString*>* photo_urls);

    QList<SWGTag*>* getTags();
    void setTags(QList<SWGTag*>* tags);

    QString* getStatus();
    void setStatus(QString* status);


    virtual bool isSet() override;

private:
    qint64 id;
    bool m_id_isSet;
    
    SWGCategory* category;
    bool m_category_isSet;
    
    QString* name;
    bool m_name_isSet;
    
    QList<QString*>* photo_urls;
    bool m_photo_urls_isSet;
    
    QList<SWGTag*>* tags;
    bool m_tags_isSet;
    
    QString* status;
    bool m_status_isSet;
    
};

}

#endif /* SWGPet_H_ */