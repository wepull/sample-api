Feature: Metering Labels API

  Background:
    Given the API is available

  Scenario: List Metering Labels
    When I send a GET request to "/v2.0/metering/metering-labels"
    Then the response status code should be 200
    And the response should be in JSON
    And the response should contain the following metering labels:
      | id                                   | tenant_id                           | description            | name   |
      | a6700594-5b7a-4105-8bfe-723b346ce866 | 45345b0ee1ea477fac0f541b2cb79cd4   | label1 description     | label1 |
      | e131d186-b02d-4c0b-83d5-0c0725c4f812 | 45345b0ee1ea477fac0f541b2cb79cd4   | label2 description     | label2 |

  Scenario: Create Metering Label
    When I send a POST request to "/v2.0/metering/metering-labels" with the following payload:
      """
      {
        "id": "bc91b832-8465-40a7-a5d8-ba87de442266",
        "tenant_id": "45345b0ee1ea477fac0f541b2cb79cd4",
        "description": "description of label1",
        "name": "label1"
      }
      """
    Then the response status code should be 201
    And the response should be in JSON
    And the response should contain the created metering label:
      | id                                   | tenant_id                           | description            | name   |
      | bc91b832-8465-40a7-a5d8-ba87de442266 | 45345b0ee1ea477fac0f541b2cb79cd4   | description of label1 | label1 |

  Scenario: Show Metering Label
    When I send a GET request to "/v2.0/metering/metering-labels/a6700594-5b7a-4105-8bfe-723b346ce866"
    Then the response status code should be 200
    And the response should be in JSON
    And the response should contain the metering label:
      | id                                   | tenant_id                           | description            | name   |
      | a6700594-5b7a-4105-8bfe-723b346ce866 | 45345b0ee1ea477fac0f541b2cb79cd4   | label1 description     | label1 |

  Scenario: Delete Metering Label
    When I send a DELETE request to "/v2.0/metering/metering-labels/a6700594-5b7a-4105-8bfe-723b346ce866"
    Then the response status code should be 204

  Scenario: List Metering Label Rules
    When I send a GET request to "/v2.0/metering/metering-label-rules"
    Then the response status code should be 200
    And the response should be in JSON
    And the response should contain the following metering label rules:
      | remote_ip_prefix | direction | metering_label_id                        | id                                   | excluded |
      | 20.0.0.0/24      | ingress   | e131d186-b02d-4c0b-83d5-0c0725c4f812   | 9536641a-7d14-4dc5-afaf-93a973ce0eb8 | false    |
      | 10.0.0.0/24      | ingress   | e131d186-b02d-4c0b-83d5-0c0725c4f812   | ffc6fd15-40de-4e7d-b617-34d3f7a93aec | false    |

  Scenario: Create Metering Label Rule
    When I send a POST request to "/v2.0/metering/metering-label-rules" with the following payload:
      """
      {
        "remote_ip_prefix": "10.0.1.0/24",
        "direction": "ingress",
        "metering_label_id": "e131d186-b02d-4c0b-83d5-0c0725c4f812",
        "id": "00e13b58-b4f2-4579-9c9c-7ac94615f9ae",
        "excluded": false
      }
      """
    Then the response status code should be 201
    And the response should be in JSON
    And the response should contain the created metering label rule:
      | remote_ip_prefix | direction | metering_label_id                        | id                                   | excluded |
      | 10.0.1.0/24      | ingress   | e131d186-b02d-4c0b-83d5-0c0725c4f812   | 00e13b58-b4f2-4579-9c9c-7ac94615f9ae | false    |

  Scenario: Show Metering Label Rule
    When I send a GET request to "/v2.0/metering/metering-label-rules/9536641a-7d14-4dc5-afaf-93a973ce0eb8"
    Then the response status code should be 200
    And the response should be in JSON
    And the response should contain the metering label rule:
      | remote_ip_prefix | direction | metering_label_id                        | id                                   | excluded |
      | 20.0.0.0/24      | ingress   | e131d186-b02d-4c0b-83d5-0c0725c4f812   | 9536641a-7d14-4dc5-afaf-93a973ce0eb8 | false    |

  Scenario: Delete Metering Label Rule
    When I send a DELETE request to "/v2.0/metering/metering-label-rules/9536641a-7d14-4dc5-afaf-93a973ce0eb8"
    Then the response status code should be 204