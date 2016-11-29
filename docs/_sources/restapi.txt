# jssample API文档

## 用户

```eval_rst

.. http:get:: /user/(user_id)

   获取用户信息

   **Example request**:

   .. sourcecode:: http

      GET /user HTTP/1.1
      Host: example.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      {
          "_id": 12345,
          "name": "hsz",
          "ctime": "2016-02-11"
      }

   :param iuser_id: 用户的id
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: optional OAuth token to authenticate
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there's no user

```
